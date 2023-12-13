from .status_validator import is_valid_status


def finalize_value(value, depth, indent):
    if isinstance(value, dict):
        stringed_value = ["{"]
        for key, inner_value in value.items():
            inner_value = finalize_value(inner_value, depth + 1, indent)
            stringed_value.append(f"{indent * (depth + 1)}{key}: {inner_value}")
        stringed_value.append(f"{indent * depth}" + "}")
        finalized_value = "\n".join(stringed_value)
    elif isinstance(value, bool):
        finalized_value = str(value).lower()
    elif value is None:
        finalized_value = 'null'
    else:
        finalized_value = value
    return finalized_value


def stylize_diff(diff, depth, indent=" ", indent_count=4):
    current_depth = depth + 1
    normal_indent = indent * indent_count
    style_indent = indent * (indent_count * current_depth - 2)
    closing_indent = normal_indent * (current_depth - 1)
    style_parts = ["{"]
    for key, diff_value in diff.items():
        inner_value = diff_value["value"]
        status = diff_value["value_status"]
        if not is_valid_status(status):
            raise ValueError('Invalid status value')
        if status != "nested":
            inner_value = finalize_value(
                inner_value, current_depth, normal_indent
            )
        match status:
            case "nested":
                style_parts.append(f"{normal_indent * current_depth}{key}: "
                                   + stylize_diff(inner_value, current_depth))
            case "added":
                style_parts.append(f"{style_indent}+ {key}: {inner_value}")
            case "removed":
                style_parts.append(f"{style_indent}- {key}: {inner_value}")
            case "same":
                style_parts.append(f"{style_indent}  {key}: {inner_value}")
            case "modified":
                inner_value2 = diff_value["new_value"]
                inner_value2 = finalize_value(
                    inner_value2, current_depth, normal_indent
                )
                style_parts.append(f"{style_indent}- {key}: {inner_value}")
                style_parts.append(f"{style_indent}+ {key}: {inner_value2}")
    style_parts.append(f"{closing_indent}" + "}")
    return "\n".join(style_parts)


def make_stylish(data):
    return stylize_diff(data, 0)
