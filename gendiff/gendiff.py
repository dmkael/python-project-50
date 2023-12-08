from gendiff.file_loader import read_local_file
from gendiff.diff_formatters import get_formatter


def build_diff_value(value1, value2, walker):
    if isinstance(value1, dict) and isinstance(value2, dict):
        value = {
            "value_status": "nested",
            "value": walker(value1, value2)
        }
    elif value1 == value2:
        value = {"value_status": "same", "value": value1}
    elif value1 == "N/A_dict1_value":
        value = {"value_status": "added", "value": value2}
    elif value2 == "N/A_dict2_value":
        value = {"value_status": "removed", "value": value1}
    else:
        value = {
            "value_status": "modified",
            "value": value1,
            "new_value": value2
        }
    return value


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sorted(set(dict1 | dict2))
    for key in sorted_keys:
        if key == "value_status":
            raise ValueError('key "value_status" is in files')
        value1 = dict1.get(key, "N/A_dict1_value")
        value2 = dict2.get(key, "N/A_dict2_value")
        diff[key] = build_diff_value(value1, value2, build_diff)
    return diff


def generate_diff(file1, file2, format_type='stylish'):
    file1 = read_local_file(file1)
    file2 = read_local_file(file2)
    formatter = get_formatter(format_type)
    return formatter(build_diff(file1, file2))
