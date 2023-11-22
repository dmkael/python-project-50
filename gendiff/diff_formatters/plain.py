from gendiff.diff_formatters.value_check import is_touched_key

CONST_LIST = ['true', 'false', 'null']


def is_str_not_const(value):
    return type(value) is str and value not in CONST_LIST


def build_plain_line(key, value, current_path):
    value = f"'{value}'" if is_str_not_const(value) else value
    value = "[complex value]" if type(value) is dict else value
    if key.startswith('+mod'):
        return f"to {value}\n"
    path = ".".join(current_path)
    if key.startswith('+add'):
        return f"Property '{path}' was added with value: {value}\n"
    if key.startswith('-rem'):
        return f"Property '{path}' was removed\n"
    if key.startswith('-mod'):
        return f"Property '{path}' was updated. From {value} "


def plain(diff):

    def walk(data, keypath):
        result = ''
        for key in data:
            value = data.get(key)
            if isinstance(value, dict) and not is_touched_key(key):
                result += walk(value, (keypath + [key]))
            else:
                str_key = str(key)[5:]
                str_line = build_plain_line(key, value, (keypath + [str_key]))
                if str_line:
                    result += str_line
        return result

    return walk(diff, []).rstrip()
