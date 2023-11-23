CONST_DICT = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def format_consts_to_str(diff_dict):
    for key in diff_dict:
        if isinstance(diff_dict[key], dict):
            format_consts_to_str(diff_dict[key])
        else:
            if CONST_DICT.get(diff_dict[key]):
                diff_dict[key] = CONST_DICT.get(diff_dict[key])
    return diff_dict
