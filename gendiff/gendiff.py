from gendiff.file_loader import load_file
from gendiff.diff_formatters import make_stylish


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


def generate_diff(file1, file2, format_dict=make_stylish):
    file1 = load_file(file1)
    file2 = load_file(file2)
    if file1 and file2:
        return format_dict(build_diff(file1, file2))
