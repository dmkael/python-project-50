import json
from .unique_keygen import UNIQUE_KEY


def build_clean_diff(data):
    if not isinstance(data, dict):
        return data
    if data.get(UNIQUE_KEY):
        data['diff_value_status'] = data.pop(UNIQUE_KEY)
    for key in data:
        build_clean_diff(data[key])
    return data


def make_json(diff):
    return json.dumps(build_clean_diff(diff))
