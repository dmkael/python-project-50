import json
import yaml


JSON_CONST_FORMATS = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def format_json(data):
    for key in data.keys():
        if isinstance(data[key], dict):
            format_json(data[key])
        else:
            if data[key] in JSON_CONST_FORMATS.keys():
                data[key] = JSON_CONST_FORMATS[data[key]]
    return data


def load_files(file1, file2):
    if file1.endswith(".json") and file2.endswith(".json"):
        json_file1 = format_json(json.load(open(file1)))
        json_file2 = format_json(json.load(open(file2)))
        return json_file1, json_file2
    if ((file1.endswith(".yaml") or file1.endswith(".yml"))
            and (file2.endswith(".yaml") or file2.endswith(".yml"))):
        yaml_file1 = yaml.safe_load(open(file1))
        yaml_file2 = yaml.safe_load(open(file2))
        return yaml_file1, yaml_file2
    return None, None
