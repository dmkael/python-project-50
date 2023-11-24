from gendiff.gendiff import generate_diff
from pathlib import Path
import json


FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_gendiff_json_to_stylish():
    file1 = FIXTURES_DIR / "file1.json"
    file2 = FIXTURES_DIR / "file2.json"
    file3 = FIXTURES_DIR / "file3.json"
    result_file1 = FIXTURES_DIR / "result1_stylish.txt"
    result_file2 = FIXTURES_DIR / "result2_stylish.txt"
    with open(result_file1, "r") as result1:
        result1 = result1.read()
        assert generate_diff(file1, file2, 'stylish') == result1
    with open(result_file2, 'r') as result2:
        result2 = result2.read()
        assert generate_diff(file1, file3, 'stylish') == result2


def test_gendiff_yaml_to_stylish():
    file1 = FIXTURES_DIR / "example1.yaml"
    file2 = FIXTURES_DIR / "example2.yml"
    result_file1 = FIXTURES_DIR / "result1_stylish.txt"
    with open(result_file1, "r") as result1:
        result = result1.read()
        assert generate_diff(file1, file2, 'stylish') == result


def test_gendiff_json_to_plain():
    file1 = FIXTURES_DIR / "file1.json"
    file2 = FIXTURES_DIR / "file2.json"
    file3 = FIXTURES_DIR / "file3.json"
    result_file1 = FIXTURES_DIR / "result1_plain.txt"
    result_file2 = FIXTURES_DIR / "result2_plain.txt"
    with open(result_file1, "r") as result1:
        result1 = result1.read()
        assert generate_diff(file1, file2, 'plain') == result1
    with open(result_file2, 'r') as result2:
        result2 = result2.read()
        assert generate_diff(file1, file3, 'plain') == result2


def test_gendiff_yaml_to_plain():
    file1 = FIXTURES_DIR / "example1.yaml"
    file2 = FIXTURES_DIR / "example2.yml"
    result_file1 = FIXTURES_DIR / "result1_plain.txt"
    with open(result_file1, "r") as result1:
        result = result1.read()
        assert generate_diff(file1, file2, 'plain') == result


def test_gendiff_json_to_json():
    file1 = FIXTURES_DIR / "file1.json"
    file2 = FIXTURES_DIR / "file2.json"
    result_file1 = FIXTURES_DIR / "result1.json"
    diff = generate_diff(file1, file2, 'json')
    with open(result_file1) as result_json:
        result = json.load(result_json)
        assert json.loads(diff) == result


def test_file_loader_for_other_files():
    file1 = FIXTURES_DIR / "file1.json"
    file2 = FIXTURES_DIR / "file4.doc"
    diff = generate_diff(file1, file2)
    assert diff == "'.doc' is not supported file type"
