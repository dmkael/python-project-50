from .unique_keygen import UNIQUE_KEY


def format_value_plain(value):
    if isinstance(value, dict):
        formatted_value = '[complex value]'
    elif isinstance(value, bool):
        formatted_value = str(value).lower()
    elif isinstance(value, (int, float)):
        formatted_value = value
    elif value is None:
        formatted_value = 'null'
    else:
        formatted_value = f"'{value}'"
    return formatted_value


def make_plain_line(value, current_path, status):
    path = ".".join(current_path)
    value1 = format_value_plain(value.get('value'))
    line = None
    match status:
        case "added":
            line = f"Property '{path}' was added with value: {value1}"
        case "removed":
            line = f"Property '{path}' was removed"
        case "modified":
            value2 = format_value_plain(value.get('to_value'))
            line = f"Property '{path}' was updated. From {value1} to {value2}"
    return line


def make_plain(diff):

    def walk(data, keypath):
        result = []
        for key, inner_value in data.items():
            status = inner_value.get(UNIQUE_KEY)
            if status == "nested":
                result.append(walk(inner_value.get('value'), keypath + [key]))
            elif status:
                str_line = make_plain_line(inner_value, keypath + [key], status)
                if str_line:
                    result.append(str_line)
        return "\n".join(result)

    return walk(diff, [])
