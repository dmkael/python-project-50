import json
from gendiff.diff_formatters.value_check import is_touched_value


def make_json(diff):

    def walk(data):
        result = {}
        for key in data:
            value = data.get(key)
            if is_touched_value(value):
                value.pop('d_key')
                result[key] = value
            else:
                result[key] = walk(value)
        return result

    return json.dumps(walk(diff))
