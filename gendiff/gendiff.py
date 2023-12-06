from gendiff.file_loader import read_local_file
from gendiff.diff_formatters import get_formatter
from gendiff.diff_formatters import UNIQUE_KEY


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sorted(set(dict1 | dict2))
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                UNIQUE_KEY: "nested",
                "value": build_diff(value1, value2)
            }
        elif key not in dict2:
            diff[key] = {UNIQUE_KEY: "removed", "value": value1}
        elif key not in dict1:
            diff[key] = {UNIQUE_KEY: "added", "value": value2}
        elif value1 == value2:
            diff[key] = {UNIQUE_KEY: "same", "value": value1}
        else:
            diff[key] = {
                UNIQUE_KEY: "modified",
                "value": value1,
                "new_value": value2
            }
    return diff


def generate_diff(file1, file2, format_type='stylish'):
    file1 = read_local_file(file1)
    file2 = read_local_file(file2)
    formatter = get_formatter(format_type)
    return formatter(build_diff(file1, file2))
