from gendiff.gendiff import generate_diff
import json


def test_gendiff_json_to_stylish():
    json_file1 = "gendiff/tests/fixtures/file1.json"
    json_file2 = "gendiff/tests/fixtures/file2.json"
    json_file3 = "gendiff/tests/fixtures/file3.json"
    result1 = "gendiff/tests/fixtures/result1_stylish.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file2, 'stylish') == result
    result2 = "gendiff/tests/fixtures/result2_stylish.txt"
    with open(result2, 'r') as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file3, 'stylish') == result


def test_gendiff_yaml_to_stylish():
    yaml_file1 = "gendiff/tests/fixtures/example1.yaml"
    yaml_file2 = "gendiff/tests/fixtures/example2.yml"
    result1 = "gendiff/tests/fixtures/result1_stylish.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(yaml_file1, yaml_file2, 'stylish') == result


def test_gendiff_json_to_plain():
    json_file1 = "gendiff/tests/fixtures/file1.json"
    json_file2 = "gendiff/tests/fixtures/file2.json"
    json_file3 = "gendiff/tests/fixtures/file3.json"
    result1 = "gendiff/tests/fixtures/result1_plain.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file2, 'plain') == result
    result2 = "gendiff/tests/fixtures/result2_plain.txt"
    with open(result2, 'r') as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file3, 'plain') == result


def test_gendiff_yaml_to_plain():
    yaml_file1 = "gendiff/tests/fixtures/example1.yaml"
    yaml_file2 = "gendiff/tests/fixtures/example2.yml"
    result1 = "gendiff/tests/fixtures/result1_plain.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(yaml_file1, yaml_file2, 'plain') == result


def test_gendiff_json_to_json():
    json_file1 = "gendiff/tests/fixtures/file1.json"
    json_file2 = "gendiff/tests/fixtures/file2.json"
    diff = generate_diff(json_file1, json_file2, 'json')
    result1 = json.load(open("gendiff/tests/fixtures/result1.json"))
    assert json.loads(diff) == result1
