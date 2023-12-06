from gendiff.gendiff import generate_diff
from pathlib import Path
import pytest
import json


FIXTURES_DIR = Path(__file__).parent / "fixtures"
json1 = FIXTURES_DIR / "file1.json"
json2 = FIXTURES_DIR / "file2.json"
json3 = FIXTURES_DIR / "file3.json"
yaml1 = FIXTURES_DIR / "example1.yaml"
yaml2 = FIXTURES_DIR / "example2.yml"
doc1 = FIXTURES_DIR / "file4.doc"
result_stylish1 = FIXTURES_DIR / "result1_stylish.txt"
result_stylish2 = FIXTURES_DIR / "result2_stylish.txt"
result_plain1 = FIXTURES_DIR / "result1_plain.txt"
result_plain2 = FIXTURES_DIR / "result2_plain.txt"
result_json1 = FIXTURES_DIR / "result1.json"


test_cases_stylish_plain = [
    ((json1, json2, 'stylish'), result_stylish1),
    ((json1, json3, 'stylish'), result_stylish2),
    ((yaml1, yaml2, 'stylish'), result_stylish1),
    ((json1, yaml2, 'stylish'), result_stylish1),
    ((yaml1, json2, 'stylish'), result_stylish1),
    ((json1, json2, 'plain'), result_plain1),
    ((json1, json3, 'plain'), result_plain2),
    ((yaml1, yaml2, 'plain'), result_plain1),
    ((json1, yaml2, 'plain'), result_plain1),
    ((yaml1, json2, 'plain'), result_plain1),
]

test_cases_json = [
    ((json1, json2, 'json'), result_json1)
]

test_cases_errors = [
    ((json1, doc1), "Unsupported file type"),
    ((json1, json2, 'something'), 'Wrong formatter')
]


@pytest.mark.parametrize("parameters, expected", test_cases_stylish_plain)
def test_gendiff_stylish_plain(parameters, expected):
    with open(expected, 'r') as result:
        assert generate_diff(*parameters) == result.read()


@pytest.mark.parametrize("parameters, expected", test_cases_json)
def test_gendiff_json(parameters, expected):
    with open(expected, 'r') as data:
        result = data.read()
        assert json.loads(generate_diff(*parameters)) == json.loads(result)


@pytest.mark.parametrize("parameters, expected", test_cases_errors)
def test_gendiff_exceptions(parameters, expected):
    with pytest.raises(Exception) as error_message:
        generate_diff(*parameters)
    assert str(error_message.value) == expected
