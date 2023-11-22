from gendiff.file_loader import load_files

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


def build_diff(dict1, dict2):
    diff = {}
    sorted_keys = sorted(dict1.keys() | dict2.keys())
    for key in sorted_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = build_diff(value1, value2)
        else:
            if key not in dict2:
                diff[f"-rem#{key}"] = value1
            elif key not in dict1:
                diff[f"+add#{key}"] = value2
            elif value1 == dict2.get(key):
                diff[f"=eql#{key}"] = value1
            else:
                diff[f"-mod#{key}"] = value1
                diff[f"+mod#{key}"] = value2
    return format_consts_to_str(diff)


def generate_diff(file1, file2, formatter):
    file1, file2 = load_files(file1, file2)
    if not file1 and not file2:
        return None
    return formatter(build_diff(file1, file2))
