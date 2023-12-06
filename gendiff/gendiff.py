from gendiff.file_loader import read_local_file
from gendiff.diff_formatters import get_formatter
from gendiff.diff_formatters import UNIQUE_KEY


def build_diff_value(value1, value2):
    if value1 == value2:
        result = {UNIQUE_KEY: "same", "value": value1}
    elif value1 == UNIQUE_KEY:
        result = {UNIQUE_KEY: "added", "value": value2}
    elif value2 == UNIQUE_KEY:
        result = {UNIQUE_KEY: "removed", "value": value1}
    else:
        result = {UNIQUE_KEY: "modified", "value": value1, "new_value": value2}
    return result


def sort_keys(dict1, dict2):
    return sorted(set(dict1 | dict2))


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sort_keys(dict1, dict2)
    for key in sorted_keys:
        value1 = dict1.get(key, UNIQUE_KEY)
        value2 = dict2.get(key, UNIQUE_KEY)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                UNIQUE_KEY: "nested",
                "value": build_diff(value1, value2)
            }
        else:
            diff[key] = build_diff_value(value1, value2)
    return diff


def generate_diff(file1, file2, format_type='stylish'):
    file1 = read_local_file(file1)
    file2 = read_local_file(file2)
    formatter = get_formatter(format_type)
    return formatter(build_diff(file1, file2))
