from .unique_keygen import UNIQUE_KEY

CONST_TRANSFORM = {
    "True": 'true',
    "False": 'false',
    "None": 'null'
}


def stringify_const(value):
    value = CONST_TRANSFORM.get(str(value), value)
    return value


def stylize_dict(value, depth, placer):
    if isinstance(value, dict):
        result = ["{"]
        for key, inner_value in value.items():
            inner_value = stylize_dict(inner_value, depth + 1, placer)
            result.append(f"{placer * (depth + 1)}{key}: {inner_value}")
        result.append(f"{placer * depth}" + "}")
        return "\n".join(result)
    value = stringify_const(value)
    return value


def build_stylish(diff, depth, placer=" ", placer_count=4):
    depth = depth + 1
    normal_placer = placer * placer_count
    mod_placer = placer * (placer_count * depth - 2)
    result = ["{"]
    for key in diff:
        value = diff[key]["value"]
        status = diff[key][UNIQUE_KEY]
        if status != "nested":
            value = stylize_dict(value, depth, normal_placer)
        match status:
            case "nested":
                result.append(f"{normal_placer * depth}{key}: "
                              + build_stylish(value, depth))
            case "added":
                result.append(f"{mod_placer}+ {key}: {value}")
            case "removed":
                result.append(f"{mod_placer}- {key}: {value}")
            case "same":
                result.append(f"{mod_placer}  {key}: {value}")
            case "modified":
                value2 = diff[key]["to_value"]
                value2 = stylize_dict(value2, depth, normal_placer)
                result.append(f"{mod_placer}- {key}: {value}")
                result.append(f"{mod_placer}+ {key}: {value2}")
    close_placer = normal_placer * (depth - 1)
    result.append(f"{close_placer}" + "}")
    return "\n".join(result)


def make_stylish(data):
    return build_stylish(data, 0)
