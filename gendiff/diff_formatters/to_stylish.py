from .unique_keygen import UNIQUE_KEY

CONST_TRANSFORM_PATTERN = {
    "True": 'true',
    "False": 'false',
    "None": 'null'
}


def transform_const(value):
    value = CONST_TRANSFORM_PATTERN.get(str(value), value)
    return value


def finalize_value(value, depth, placer):
    if not isinstance(value, dict):
        value = transform_const(value)
        return value
    result = ["{"]
    for key, inner_value in value.items():
        inner_value = finalize_value(inner_value, depth + 1, placer)
        result.append(f"{placer * (depth + 1)}{key}: {inner_value}")
    result.append(f"{placer * depth}" + "}")
    return "\n".join(result)


def stylize_diff(diff, depth, placer=" ", placer_count=4):
    depth = depth + 1
    normal_placer = placer * placer_count
    mod_placer = placer * (placer_count * depth - 2)
    result = ["{"]
    for key in diff:
        inner_value = diff[key]["value"]
        status = diff[key][UNIQUE_KEY]
        if status != "nested":
            inner_value = finalize_value(inner_value, depth, normal_placer)
        match status:
            case "nested":
                result.append(f"{normal_placer * depth}{key}: "
                              + stylize_diff(inner_value, depth))
            case "added":
                result.append(f"{mod_placer}+ {key}: {inner_value}")
            case "removed":
                result.append(f"{mod_placer}- {key}: {inner_value}")
            case "same":
                result.append(f"{mod_placer}  {key}: {inner_value}")
            case "modified":
                inner_value2 = diff[key]["new_value"]
                inner_value2 = finalize_value(
                    inner_value2, depth, normal_placer
                )
                result.append(f"{mod_placer}- {key}: {inner_value}")
                result.append(f"{mod_placer}+ {key}: {inner_value2}")
    close_placer = normal_placer * (depth - 1)
    result.append(f"{close_placer}" + "}")
    return "\n".join(result)


def make_stylish(data):
    return stylize_diff(data, depth=0)
