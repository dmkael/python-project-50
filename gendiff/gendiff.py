import json
from gendiff.json_diff import json_diff


def generate_diff(file1, file2):
    if file1[-5:] == ".json" and file2[-5:] == ".json":
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
        result = dict_to_str(json_diff(file1, file2))
        return result
    else:
        return "other file types under development"


def dict_to_str(input_dict):
    result_str = "{"
    if input_dict:
        for key in input_dict:
            result_str += f"\n{key}: {input_dict[key]}"
    result_str = result_str + "\n}"
    return result_str
