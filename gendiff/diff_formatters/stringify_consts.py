def format_consts_to_str(diff_dict):
    for key in diff_dict:
        value = diff_dict[key]
        if isinstance(value, dict):
            format_consts_to_str(value)
        if isinstance(value, bool):
            diff_dict[key] = str(value).lower()
        if value is None:
            diff_dict[key] = 'null'
    return diff_dict
