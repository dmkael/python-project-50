def get_json_diff(file1, file2):
    all_keys = sorted(file1 | file2)
    result_dict = {}
    for key in all_keys:
        if file1.get(key) == file2.get(key):
            result_dict[f"{key}"] = file1.get(key)
        else:
            if key in file1:
                result_dict[f"-{key}"] = file1.get(key)
            if key in file2:
                result_dict[f"+{key}"] = file2.get(key)
    return result_dict
