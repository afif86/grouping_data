from flask import Flask, render_template, request
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

# creates a Flask application
app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def insertData():
    return render_template('index.html')


def analyse_data(data=None, file=None):
    """
    This function takes in a json string and/or a csv file and returns a list of strings.
    The json string and/or csv file contains a list of name/address pairs.
    """
    df_json = pd.DataFrame()
    df_file = pd.DataFrame()
    if data:
        data = json.loads(data)
        df_json = pd.json_normalize(data)
        df_json.columns = map(str.lower, df_json.columns)
    if file:
        df_file = pd.read_csv(file, encoding='utf8')
        df_file.columns = map(str.lower, df_file.columns)

    if df_file.empty == False and df_json.empty == False:
        # concat 2 dataframes together
        df = pd.concat([df_file, df_json], axis=0, ignore_index=True)
    elif df_file.empty == False:
        df = df_file
    elif df_json.empty == False:
        df = df_json

    # drop duplicates
    df.drop_duplicates(subset=['name', 'address'], keep='first', inplace=True)

    # get dpbc for each address
    df['dpbc'] = df.apply(lambda row: get_dpbc(row['address']), axis=1)

    # drop rows with invalid address
    if df.isnull().values.any():
        raise ValueError("Some name/addresses are not valid")

    # drop rows with empty name or address
    df.dropna(subset=['name', 'address'], inplace=True)

    # sort by dpbc
    initialList = df.groupby('dpbc')['name'].apply(
        lambda x: x.sort_values().values).to_list()
    initialList.sort(key=lambda x: x[0])
    result = []
    for item in initialList:
        result.append(', '.join(item.tolist()))

    return result

# get a csv file from the user


@app.route("/saved", methods=['POST'])
def saved():
    file = request.files.get("file")
    data = request.form.get("data")

    result = analyse_data(data, file)

    # save result to a file
    result_path = os.path.join(BASE_DIR, "static", 'result.txt')
    with open(result_path, 'w', encoding="utf-8") as file:
        for item in result:
            file.write("%s\n" % item)

    return render_template('result.html', result=result)


def get_dpbc(address):
    """
    This function takes in an address and returns the dpbc of the address, using google Geolocation API.
    dpbc stands for "Dissemination Area Postal Code".
    """

    res = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+API_KEY)
    if res.status_code != 200:
        return None
    data = res.json()
    try:
        output = data['results'][0]['geometry']['location']
    except IndexError:
        return None
    return round(output['lat'], 2), round(output['lng'], 2)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
