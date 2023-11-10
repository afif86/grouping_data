<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Grouping Data</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)


</div>

---

<p align="center"> a web application which get your data as a csv file or manual input and group them based on the address
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)


## 🧐 About <a name = "about"></a>

A webapp which groups people living at identical addresses and return the result sorted alphabetically.  
## Features
The webapp provide two ways to input the data: 
- By manual text entry through the form 
- By uploading а .csv file. 
- Using both option at the same time. 
..
The results will display on the UI and users have an option to download the results as a .txt file.
A text document where each line is a comma-separated list of names of people living at the same address. 
The names on each line is sorted alphabetically. 
The lines of the file also is sorted alphabetically.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Usage](#usage) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.9 +
Some kind of virtual environment like pipenv, venv , ... (Optional/ Recommended)
Google Geolocation API

```


### Installing

Create a virtual environment then install the requirements, (following the commands)

```
pip install -r requirements.text
```
change the env.sample to .env and add the google API key to it. 
**Hint:** get the google API from here: https://developers.google.com/maps/documentation/geolocation/get-api-key


## 🔧 Running the tests <a name = "tests"></a>


Execute by following command: 

```
pytest
```


## 🎈 Usage <a name="usage"></a>

Add your data through table one by one or upload a csv file and submit, the result will appear in a seconds. 

Use **flask run** command to run the app. it will listen on your local host port: 5000 by default, to change the port execute the following command:

```
flask run -p _yourDesireNumber_
```


