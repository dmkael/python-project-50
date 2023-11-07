import json
from gendiff.json_diff import get_json_diff


def generate_diff(file1, file2):
    if file1.endswith(".json") and file2.endswith(".json"):
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
        result = dict_to_str(get_json_diff(file1, file2))
        return result
    else:
        return "in development"


def dict_to_str(input_dict):
    result_str = "{"
    if input_dict:
        for key in input_dict:
            if input_dict[key] is True:
                input_dict[key] = 'true'
            if input_dict[key] is False:
                input_dict[key] = 'false'
            result_str += f"\n{key}: {input_dict[key]}"
    result_str = result_str + "\n}"
    return result_str
