from .status_key import STATUS_KEY


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


def make_plain_line(value, current_path, status, walker):
    path = ".".join(current_path)
    value1 = value.get('value')
    line = None
    if status == "nested":
        line = walker(value1, current_path)
    elif status == "added":
        line = (f"Property '{path}' "
                f"was added with value: {format_value_plain(value1)}")
    elif status == "removed":
        line = f"Property '{path}' was removed"
    elif status == "modified":
        value2 = value.get('new_value')
        line = (f"Property '{path}' was updated. "
                f"From {format_value_plain(value1)} "
                f"to {format_value_plain(value2)}")
    return line


def make_plain(diff):

    def walk(data, keypath):
        result = []
        for key, inner_value in data.items():
            status = inner_value.get(STATUS_KEY)
            value = make_plain_line(inner_value, keypath + [key], status, walk)
            if value:
                result.append(value)
        return "\n".join(result)

    return walk(diff, [])
