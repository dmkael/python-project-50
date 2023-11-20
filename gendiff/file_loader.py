import json
import yaml


JSON_CONST = {
    True: 'true',
    False: 'false',
    None: 'null'
}

YAML_CONST = {
    None: 'null'
}


def format_consts(data, dict_type):
    for key in data.keys():
        if isinstance(data[key], dict):
            format_consts(data[key], dict_type)
        else:
            if data[key] in dict_type.keys():
                data[key] = dict_type[data[key]]
    return data


def load_files(file1, file2):
    if file1.endswith(".json") and file2.endswith(".json"):
        json_file1 = format_consts(json.load(open(file1)), JSON_CONST)
        json_file2 = format_consts(json.load(open(file2)), JSON_CONST)
        return json_file1, json_file2
    if ((file1.endswith(".yaml") or file1.endswith(".yml"))
            and (file2.endswith(".yaml") or file2.endswith(".yml"))):
        yaml_file1 = format_consts(yaml.safe_load(open(file1)), YAML_CONST)
        yaml_file2 = format_consts(yaml.safe_load(open(file2)), YAML_CONST)
        return yaml_file1, yaml_file2
    return None, None
