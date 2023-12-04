from gendiff.file_loader import read_local_file
from gendiff.diff_formatters import get_formatter


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sorted(dict1.keys() | dict2.keys())
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = build_diff(value1, value2)
        elif key not in dict2:
            diff[key] = {"status": "removed", "d_key": key, "value": value1}
        elif key not in dict1:
            diff[key] = {"status": "added", "d_key": key, "value": value2}
        elif value1 == value2:
            diff[key] = {"status": "same", "d_key": key, "value": value1}
        else:
            diff[key] = {
                "status": "modified",
                "d_key": key,
                "value": value1,
                "value_new": value2
            }
    return diff


def generate_diff(file1, file2, format_type='stylish'):
    file1 = read_local_file(file1)
    file2 = read_local_file(file2)
    formatter = get_formatter(format_type)
    return formatter(build_diff(file1, file2))
