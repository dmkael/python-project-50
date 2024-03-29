from .to_stylish import make_stylish
from .to_plain import make_plain
from .to_json import make_json


def get_formatter(formatter_name):
    if formatter_name == 'plain':
        return make_plain
    if formatter_name == 'stylish':
        return make_stylish
    if formatter_name == 'json':
        return make_json
    raise ValueError('Wrong formatter')
