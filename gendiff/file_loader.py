import json
import yaml


def load_files(file1, file2):
    if file1.endswith(".json") and file2.endswith(".json"):
        json_file1 = json.load(open(file1))
        json_file2 = json.load(open(file2))
        return json_file1, json_file2
    if ((file1.endswith(".yaml") or file1.endswith(".yml"))
            and (file2.endswith(".yaml") or file2.endswith(".yml"))):
        yaml_file1 = yaml.safe_load(open(file1))
        yaml_file2 = yaml.safe_load(open(file2))
        return yaml_file1, yaml_file2
    return None, None
