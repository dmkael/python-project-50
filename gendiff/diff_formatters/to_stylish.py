from gendiff.diff_formatters.value_check import is_touched_value


def format_values_stylish(data_dict):
    for key, value in data_dict.items():
        if isinstance(value, dict):
            format_values_stylish(value)
        elif isinstance(value, bool):
            data_dict[key] = str(value).lower()
        elif value is None:
            data_dict[key] = 'null'
    return data_dict


def make_stylish_line(data, depth, placer, placer_count, walker_func):
    current_status = data.get('status')
    indention = placer * (placer_count * depth - 2)
    line = None
    if isinstance(data['value'], dict):
        value = walker_func(data['value'], depth)
    else:
        value = data['value']
    match current_status:
        case 'added':
            line = f"{indention}+ {data['d_key']}: {value}"
        case 'removed':
            line = f"{indention}- {data['d_key']}: {value}"
        case 'same':
            line = f"{indention}  {data['d_key']}: {value}"
        case 'modified':
            if isinstance(data['value_new'], dict):
                value2 = walker_func(data['value_new'], depth)
            else:
                value2 = data['value_new']
            line1 = f"{indention}- {data['d_key']}: {value}\n"
            line2 = f"{indention}+ {data['d_key']}: {value2}"
            line = line1 + line2
    return line


def make_stylish(data, placer=" ", placer_count=4):
    data = format_values_stylish(data)

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        result = ["{"]
        depth += 1
        for key in current_value:
            if is_touched_value(current_value[key]):
                touched_value = current_value[key]
                result.append(
                    make_stylish_line(
                        touched_value, depth, placer, placer_count, walk
                    )
                )
            else:
                str_key = f"{placer * placer_count * depth}{key}"
                str_value = f"{walk(current_value[key], depth)}"
                line = f"{str_key}: {str_value}"
                result.append(line)
        result.append(f"{placer * placer_count * (depth - 1)}" + "}")
        return '\n'.join(result)

    return walk(data, 0)
