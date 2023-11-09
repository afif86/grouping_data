# import analyse_data function from app.py
from app import analyse_data, get_dpbc
import pytest


def test_analyse_data_with_sample_csv():
    with open("sample_input.csv", "r", encoding="utf-8") as sample_file:
        result = analyse_data(None, sample_file)
    
    # check the result
    assert result == ["Dragan Doichinov, Ilona Ilieva, Ivan Draganov", "Frieda Müller", "Leon Wu, Li Deng"]


def test_analyse_data_with_sample_json():
    with open("sample_input.json", "r", encoding="utf-8") as sample_file:
        result = analyse_data(sample_file.read(), None)
    
    # check the result
    assert result == ["Dragan Doichinov, Ilona Ilieva, Ivan Draganov", "Frieda Müller", "Leon Wu, Li Deng"]


def test_analyse_data_with_sample_csv_and_json():
    # testing uniqueness and calling analyse data with both csv and json
    with open("sample_input.csv", "r", encoding="utf-8") as sample_file_csv:
        with open("sample_input.json", "r", encoding="utf-8") as sample_file_json:
            result = analyse_data(sample_file_json.read(), sample_file_csv)
    
    # check the result
    assert result == ["Dragan Doichinov, Ilona Ilieva, Ivan Draganov", "Frieda Müller", "Leon Wu, Li Deng"] 


def test_get_dpbc():
    # test with a sample address
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    dpbc = get_dpbc(address)
    assert dpbc == (37.42, -122.08)

