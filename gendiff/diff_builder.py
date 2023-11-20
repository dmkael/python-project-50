def value_stub():
    return


def build_diff(dict1, dict2):
    result_dict = {}
    default_value = value_stub
    for key in sorted(dict1.keys() | dict2.keys()):
        value1 = dict1.get(key, default_value)
        value2 = dict2.get(key, default_value)
        if value1 == value2:
            result_dict[f"  {key}"] = value1
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                result_dict[key] = build_diff(value1, value2)
            else:
                if value1 is not default_value:
                    result_dict[f"- {key}"] = value1
                if value2 is not default_value:
                    result_dict[f"+ {key}"] = value2
    return result_dict