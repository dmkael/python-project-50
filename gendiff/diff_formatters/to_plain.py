from gendiff.diff_formatters.value_check import is_touched_value


def format_value_plain(value):
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, (int, float)):
        result = value
    elif value is None:
        result = 'null'
    else:
        result = f"'{value}'"
    return result


def build_plain_line(value, current_path):
    current_state = value.get('status')
    path = ".".join(current_path)
    value1 = format_value_plain(value.get('value'))
    result = None
    match current_state:
        case "added":
            result = f"Property '{path}' was added with value: {value1}"
        case "removed":
            result = f"Property '{path}' was removed"
        case "modified":
            value2 = format_value_plain(value.get('value_new'))
            result = f"Property '{path}' was updated. From {value1} to {value2}"
    return result


def make_plain(diff):

    def walk(data, keypath):
        result = []
        for key in data:
            value = data.get(key)
            if is_touched_value(value):
                str_line = build_plain_line(value, (keypath + [key]))
                if str_line:
                    result.append(str_line)
            else:
                result.append(walk(value, (keypath + [key])))
        return "\n".join(result)

    return walk(diff, [])
