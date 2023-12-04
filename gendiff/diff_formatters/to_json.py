import json
from gendiff.diff_formatters.value_check import is_touched_value


def prebuild_clean_diff(data):
    result = {}
    for key in data:
        value = data.get(key)
        if is_touched_value(value):
            value.pop('d_key')
            result[key] = value
        else:
            result[key] = prebuild_clean_diff(value)
    return result


def make_json(diff):
    return json.dumps(prebuild_clean_diff(diff))
