from .unique_keygen import UNIQUE_KEY

CONST_TRANSFORM_PATTERN = {
    "True": 'true',
    "False": 'false',
    "None": 'null'
}


def finalize_value(value, depth, indent):
    if not isinstance(value, dict):
        value = CONST_TRANSFORM_PATTERN.get(str(value), value)
        return value
    result = ["{"]
    for key, inner_value in value.items():
        inner_value = finalize_value(inner_value, depth + 1, indent)
        result.append(f"{indent * (depth + 1)}{key}: {inner_value}")
    result.append(f"{indent * depth}" + "}")
    return "\n".join(result)


def make_stylish_value(status, indent, key, values):
    value1, value2 = values
    stylish_value = None
    if status == "added":
        stylish_value = f"{indent}+ {key}: {value1}"
    elif status == "removed":
        stylish_value = f"{indent}- {key}: {value1}"
    elif status == "same":
        stylish_value = f"{indent}  {key}: {value1}"
    elif status == "modified":
        stylish_part1 = f"{indent}- {key}: {value1}\n"
        stylish_part2 = f"{indent}+ {key}: {value2}"
        stylish_value = stylish_part1 + stylish_part2
    return stylish_value


def stylize_diff(diff, depth, indent=" ", indent_count=4):
    result = ["{"]
    current_depth = depth + 1
    normal_indent = indent * indent_count
    mod_indent = indent * (indent_count * current_depth - 2)
    closing_indent = normal_indent * (current_depth - 1)

    for key, diff_value in diff.items():
        value = diff_value.get("value", UNIQUE_KEY)
        value2 = diff_value.get("new_value", UNIQUE_KEY)
        status = diff_value[UNIQUE_KEY]
        if status == "nested":
            result.append(f"{normal_indent * current_depth}{key}: "
                          + stylize_diff(value, current_depth))
        else:
            value = finalize_value(value, current_depth, normal_indent)
            if value2 != UNIQUE_KEY:
                value2 = finalize_value(value2, current_depth, normal_indent)
            values = value, value2
            result.append(make_stylish_value(status, mod_indent, key, values))

    result.append(f"{closing_indent}" + "}")
    return "\n".join(result)


def make_stylish(data):
    return stylize_diff(data, depth=0)
