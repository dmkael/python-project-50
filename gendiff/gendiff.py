from gendiff.files_loader import load_files
from gendiff.dict_comparer import compare_dicts


def generate_diff(file1, file2):
    file1, file2 = load_files(file1, file2)
    if not file1 and not file2:
        return "Files types are different or file(s) are empty"
    return dict_to_str(compare_dicts(file1, file2))


def dict_to_str(input_dict):
    result_str = "{"
    if input_dict:
        for key in input_dict:
            if input_dict[key] is True:
                input_dict[key] = 'true'
            if input_dict[key] is False:
                input_dict[key] = 'false'
            result_str += f"\n{key}: {input_dict[key]}"
    result_str = result_str + "\n}"
    return result_str
