def is_touched_value(key):
    mod_keys = ['=eql#', '+add#', '-rem#', '-mod#', '+mod#']
    return any(key.startswith(x) for x in mod_keys)


def format_stylish_key(key):
    shorten_key = key[5:]
    if key.startswith('=eql#'):
        return "  " + shorten_key
    if key.startswith('+add#') or key.startswith('+mod#'):
        return "+ " + shorten_key
    if key.startswith('-rem#') or key.startswith('-mod#'):
        return "- " + shorten_key


def format_plain_value(key, value, current_path):
    path = ".".join(current_path)
    value = f"'{value}'" if type(value) is str else value
    if isinstance(value, dict):
        value = "[complex value]"
    if key.startswith('+add'):
        return f"Property '{path}' was added with value: {value}\n"
    if key.startswith('-rem'):
        return f"Property '{path}' was removed\n"
    if key.startswith('-mod'):
        return f"Property '{path}' was updated. From {value} "
    if key.startswith('+mod'):
        return f"to {value}\n"


def stylish(data, replacer=" ", quantity=4):
    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        result = "{\n"
        for key in current_value:
            if is_touched_value(key):
                str_key = (f"{replacer * (quantity * (depth + 1) - 2)}"
                           f"{format_stylish_key(key)}")
            else:
                str_key = f"{replacer * quantity * (depth + 1)}{key}"
            str_value = f"{walk(current_value[key], (depth + 1))}\n"
            result += f"{str_key}: {str_value}"
        return result + f"{replacer * quantity * depth}" + "}"

    return walk(data, 0)


def plain(diff):
    path = []

    def walk(data, keypath):
        result = ''
        for key in data:
            value = data.get(key)
            if isinstance(value, dict) and not is_touched_value(key):
                result += walk(value, (keypath + [key]))
            else:
                str_key = str(key)[5:]
                str_line = format_plain_value(key, value, (keypath + [str_key]))
                if str_line:
                    result += str_line
        return result

    return walk(diff, path)
