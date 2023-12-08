import json


def build_clean_diff(data):
    if not isinstance(data, dict):
        return data
    if data.get("status_key"):
        data['diff_value_status'] = data.pop("status_key")
    for key in data:
        build_clean_diff(data[key])
    return data


def make_json(diff):
    return json.dumps(build_clean_diff(diff))
