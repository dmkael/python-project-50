from gendiff.diff_formatters.value_check import is_touched_key
from gendiff.diff_formatters.stringify_consts import format_consts_to_str


def format_stylish_key(key):
    original_key = key[5:]
    if key.startswith('=eql#'):
        return "  " + original_key
    if key.startswith('+add#') or key.startswith('+mod#'):
        return "+ " + original_key
    if key.startswith('-rem#') or key.startswith('-mod#'):
        return "- " + original_key


def stylish(data, replacer=" ", quantity=4):
    data = format_consts_to_str(data)

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        result = "{\n"
        for key in current_value:
            if is_touched_key(key):
                str_key = (f"{replacer * (quantity * (depth + 1) - 2)}"
                           f"{format_stylish_key(key)}")
            else:
                str_key = f"{replacer * quantity * (depth + 1)}{key}"
            str_value = f"{walk(current_value[key], (depth + 1))}\n"
            result += f"{str_key}: {str_value}"
        return result + f"{replacer * quantity * depth}" + "}"

    return walk(data, 0)
