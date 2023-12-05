import json
from .value_check import is_touched_value
from .unique_keygen import UNIQUE_KEY


def prebuild_clean_diff(data):
    result = {}
    for key in data:
        value = data.get(key)
        if is_touched_value(value):
            value.pop('d_key')
            value['diff_value_status'] = value.pop(UNIQUE_KEY)
            result[key] = value
        else:
            result[key] = prebuild_clean_diff(value)
    return result


def make_json(diff):
    return json.dumps(prebuild_clean_diff(diff))
