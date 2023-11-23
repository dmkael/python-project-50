from gendiff.file_loader import load_file
from gendiff.diff_formatters import make_stylish, make_plain, make_json


def get_formatter(user_input):
    if user_input == 'plain':
        return make_plain
    if user_input == 'stylish':
        return make_stylish
    if user_input == 'json':
        return make_json
    return "Wrong formatter parameter"


def check_inputs(file1, file2, formatter):
    error_message = []
    if type(file1) is str:
        error_message += [file1]
    if type(file2) is str:
        error_message += [file2]
    if formatter == "Wrong formatter parameter":
        error_message += [formatter]
    if error_message:
        return False, "\n".join(error_message)
    return True, "Correct"


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sorted(dict1.keys() | dict2.keys())
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = build_diff(value1, value2)
        else:
            if key not in dict2:
                diff[f"-rem#{key}"] = value1
            elif key not in dict1:
                diff[f"+add#{key}"] = value2
            elif value1 == dict2.get(key):
                diff[f"=eql#{key}"] = value1
            else:
                diff[f"-mod#{key}"] = value1
                diff[f"+mod#{key}"] = value2
    return diff


def generate_diff(file1, file2, format_type='stylish'):
    file1 = load_file(file1)
    file2 = load_file(file2)
    formatter = get_formatter(format_type)
    valid_input, error_message = check_inputs(file1, file2, formatter)
    if valid_input:
        return formatter(build_diff(file1, file2))
    return error_message
