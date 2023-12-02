from gendiff.gendiff import generate_diff
from pathlib import Path
import json
import pytest


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


test_cases_stylish = [
    ((json1, json2), result_stylish1),
    ((json1, json3), result_stylish2),
    ((yaml1, yaml2), result_stylish1),
    ((json1, yaml2), result_stylish1),
    ((yaml1, json2), result_stylish1)
]

test_cases_plain = [
    ((json1, json2), result_plain1),
    ((json1, json3), result_plain2),
    ((yaml1, yaml2), result_plain1),
    ((json1, yaml2), result_plain1),
    ((yaml1, json2), result_plain1)
]

test_cases_json = [
    ((json1, json2), result_json1)
]


@pytest.mark.parametrize("files, expected", test_cases_stylish)
def test_gendiff_stylish(files, expected):
    with open(expected, 'r') as result:
        assert generate_diff(*files) == result.read()


@pytest.mark.parametrize("files, expected", test_cases_plain)
def test_gendiff_plain(files, expected):
    with open(expected, 'r') as result:
        assert generate_diff(*files, "plain") == result.read()


@pytest.mark.parametrize("files, expected", test_cases_json)
def test_gendiff_json(files, expected):
    with open(expected, 'r') as data:
        result = data.read()
        assert json.loads(generate_diff(*files, "json")) == json.loads(result)


def test_gendiff_exceptions():
    with pytest.raises(Exception) as error_message:
        generate_diff(json1, doc1)
        assert str(error_message) == 'Unsupported file type'
        generate_diff(json1, json2, "something")
        assert str(error_message) == 'Wrong formatter'
