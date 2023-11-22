from gendiff.gendiff import generate_diff
from gendiff.diff_formatters import stylish


def test_gendiff_json():
    json_file1 = "gendiff/tests/fixtures/file1.json"
    json_file2 = "gendiff/tests/fixtures/file2.json"
    json_file3 = "gendiff/tests/fixtures/file3.json"
    result1 = "gendiff/tests/fixtures/result1_json.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file2, stylish) == result
    result2 = "gendiff/tests/fixtures/result2_json.txt"
    with open(result2, 'r') as txt:
        result = txt.read()
        assert generate_diff(json_file1, json_file3, stylish) == result


def test_gendiff_yaml():
    yaml_file1 = "gendiff/tests/fixtures/example1.yaml"
    yaml_file2 = "gendiff/tests/fixtures/example2.yml"
    result1 = "gendiff/tests/fixtures/result1_yaml.txt"
    with open(result1, "r") as txt:
        result = txt.read()
        assert generate_diff(yaml_file1, yaml_file2, stylish) == result
