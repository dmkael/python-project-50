from gendiff.gendiff import generate_diff
from pathlib import Path
import pytest
import json


FIXTURES_DIR = Path(__file__).parent / "fixtures"
json1 = FIXTURES_DIR / "file1.json"
json2 = FIXTURES_DIR / "file2.json"
json3 = FIXTURES_DIR / "file3.json"
json4 = FIXTURES_DIR / "file4.json"
yaml1 = FIXTURES_DIR / "example1.yaml"
yaml2 = FIXTURES_DIR / "example2.yml"
doc1 = FIXTURES_DIR / "file4.doc"
result_stylish1 = FIXTURES_DIR / "result1_stylish.txt"
result_stylish2 = FIXTURES_DIR / "result2_stylish.txt"
result_plain1 = FIXTURES_DIR / "result1_plain.txt"
result_plain2 = FIXTURES_DIR / "result2_plain.txt"
result_json1 = FIXTURES_DIR / "result1.json"

test_cases_raw = [
    ((json1, json2, 'stylish'), result_stylish1),
    ((json1, json3, 'stylish'), result_stylish2),
    ((yaml1, yaml2, 'stylish'), result_stylish1),
    ((json1, yaml2, 'stylish'), result_stylish1),
    ((yaml1, json2, 'stylish'), result_stylish1),
    ((json1, json2, 'plain'), result_plain1),
    ((json1, json3, 'plain'), result_plain2),
    ((yaml1, yaml2, 'plain'), result_plain1),
    ((json1, yaml2, 'plain'), result_plain1),
    ((yaml1, json2, 'plain'), result_plain1)
]

test_cases_files = [
    ((json1, json2, 'json'), json.loads, result_json1),
    ((yaml1, yaml2, 'json'), json.loads, result_json1),
    ((json1, yaml2, 'json'), json.loads, result_json1),
    ((yaml1, json2, 'json'), json.loads, result_json1)
]

test_cases_errors = [
    ((json1, doc1), "Unsupported file type"),
    ((json1, json2, 'something'), 'Wrong formatter'),
    ((json1, json4), "Wrong data in file")
]


@pytest.mark.parametrize("parameters, expected", test_cases_raw)
def test_gendiff_raw_data(parameters, expected):
    with open(expected, 'r') as result:
        assert generate_diff(*parameters) == result.read()


@pytest.mark.parametrize("parameters, loader, expected", test_cases_files)
def test_gendiff_file_data(parameters, loader, expected):
    with open(expected, 'r') as data:
        file = data.read()
        assert loader(generate_diff(*parameters)) == loader(file)


@pytest.mark.parametrize("parameters, expected", test_cases_errors)
def test_gendiff_exceptions(parameters, expected):
    with pytest.raises(Exception) as error_message:
        generate_diff(*parameters)
    assert str(error_message.value) == expected
