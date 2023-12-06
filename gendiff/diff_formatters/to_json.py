import json
from .unique_keygen import UNIQUE_KEY


def build_clean_diff(data):
    for key, inner_value in data.items():
        if isinstance(inner_value, dict):
            build_clean_diff(inner_value)
            status = inner_value.get(UNIQUE_KEY)
            if status:
                inner_value['diff_value_status'] = inner_value.pop(UNIQUE_KEY)
            if status == 'same' or status == 'nested':
                data[key] = inner_value.get('value')
    return data


def make_json(diff):
    return json.dumps(build_clean_diff(diff))
