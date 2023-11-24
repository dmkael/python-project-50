from gendiff.gendiff import generate_diff
import json


def test_gendiff_json_to_stylish(get_fixtures_dir):
    file1 = get_fixtures_dir / "file1.json"
    file2 = get_fixtures_dir / "file2.json"
    file3 = get_fixtures_dir / "file3.json"
    result_file1 = get_fixtures_dir / "result1_stylish.txt"
    result_file2 = get_fixtures_dir / "result2_stylish.txt"
    with open(result_file1, "r") as result1:
        result1 = result1.read()
        assert generate_diff(file1, file2, 'stylish') == result1
    with open(result_file2, 'r') as result2:
        result2 = result2.read()
        assert generate_diff(file1, file3, 'stylish') == result2


def test_gendiff_yaml_to_stylish(get_fixtures_dir):
    file1 = get_fixtures_dir / "example1.yaml"
    file2 = get_fixtures_dir / "example2.yml"
    result_file1 = get_fixtures_dir / "result1_stylish.txt"
    with open(result_file1, "r") as result1:
        result = result1.read()
        assert generate_diff(file1, file2, 'stylish') == result


def test_gendiff_json_to_plain(get_fixtures_dir):
    file1 = get_fixtures_dir / "file1.json"
    file2 = get_fixtures_dir / "file2.json"
    file3 = get_fixtures_dir / "file3.json"
    result_file1 = get_fixtures_dir / "result1_plain.txt"
    result_file2 = get_fixtures_dir / "result2_plain.txt"
    with open(result_file1, "r") as result1:
        result1 = result1.read()
        assert generate_diff(file1, file2, 'plain') == result1
    with open(result_file2, 'r') as result2:
        result2 = result2.read()
        assert generate_diff(file1, file3, 'plain') == result2


def test_gendiff_yaml_to_plain(get_fixtures_dir):
    file1 = get_fixtures_dir / "example1.yaml"
    file2 = get_fixtures_dir / "example2.yml"
    result_file1 = get_fixtures_dir / "result1_plain.txt"
    with open(result_file1, "r") as result1:
        result = result1.read()
        assert generate_diff(file1, file2, 'plain') == result


def test_gendiff_json_to_json(get_fixtures_dir):
    file1 = get_fixtures_dir / "file1.json"
    file2 = get_fixtures_dir / "file2.json"
    result_file1 = get_fixtures_dir / "result1.json"
    diff = generate_diff(file1, file2, 'json')
    with open(result_file1) as result_json:
        result = json.load(result_json)
        assert json.loads(diff) == result


def test_file_loader_for_other_files(get_fixtures_dir):
    file1 = get_fixtures_dir / "file1.json"
    file2 = get_fixtures_dir / "file4.doc"
    diff = generate_diff(file1, file2)
    assert diff == "'.doc' is not supported file type"
