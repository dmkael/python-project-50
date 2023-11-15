def compare_dicts(dict1, dict2):
    all_keys = sorted(dict1 | dict2)
    result_dict = {}
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if value1 == value2:
            result_dict[f"    {key}"] = value1
        else:
            if value1 is not None:
                result_dict[f"  - {key}"] = value1
            if value2 is not None:
                result_dict[f"  + {key}"] = value2
    return result_dict
