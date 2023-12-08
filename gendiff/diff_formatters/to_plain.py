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
            status = inner_value.get("value_status")
            # а действительно ли нужно
            # проверять status на ValueError?
            # В gendiff значение сейчас всегда
            # проваливается в словарь с ключом "value"
            # в котором так же будет ключ "value_status"
            # только с заданными состояниями.
            # Даже если в исходном словаре из файла
            # будет ключ "value_status": 'status'
            # то при построении диффа значение
            # провалится в словарь с ключом "value".
            # Т.е. при разборе значение "value_status"
            # может быть только 'status'
            # А исходные значения всегда только словаре
            # в ключе 'value', будь там что угодно.
            # Т.е. если в gendiff подсунуть его же результаты
            # То он сложит всё правильно.
            # В моей первой реализации это было актуально,
            # Т.к. я там нагородил не очень грамотную реализацию.
            value = make_plain_line(inner_value, keypath + [key], status, walk)
            if value:
                result.append(value)
        return "\n".join(result)

    return walk(diff, [])
