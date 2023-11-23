def format_consts_to_str(diff_dict):
    for key in diff_dict:
        if isinstance(diff_dict[key], dict):
            format_consts_to_str(diff_dict[key])
        if isinstance(diff_dict[key], bool):
            diff_dict[key] = str(diff_dict[key]).lower()
        if diff_dict[key] is None:
            diff_dict[key] = 'null'
    return diff_dict
