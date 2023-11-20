from gendiff.file_loader import load_files
from gendiff.diff_builder import build_diff


def stylish(data, replacer=" ", quantity=4):

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        result = "{\n"
        for key in current_value:
            temp_key = str(key)
            if any(temp_key.startswith(x) for x in [' ', '+ ', '- ']):
                str_key = f"{replacer * (quantity * (depth + 1) - 2)}{temp_key}"
            else:
                str_key = f"{replacer * quantity * (depth + 1)}{temp_key}"
            str_value = f"{walk(current_value[key], (depth + 1))}\n"
            result += f"{str_key}: {str_value}"
        return result + f"{replacer * quantity * depth}" + "}"

    return walk(data, 0)


def generate_diff(file1, file2, formatter=stylish):
    file1, file2 = load_files(file1, file2)
    if not file1 and not file2:
        return "Files types are different or file(s) are empty"
    return formatter(build_diff(file1, file2))
