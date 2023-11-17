from gendiff.file_loader import load_files
from gendiff.diff_builder import build_diff


def stylish(data, replacer=" ", space_counter=1):
    replacer = replacer * space_counter

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        result = "{\n"
        for key in current_value:
            str_key = f"{replacer * (depth + 1)}{str(key)}"
            str_value = f"{walk(current_value[key], (depth + 1))}\n"
            result += f"{str_key}: {str_value}"
        return result + f"{replacer * depth}" + "}"

    return walk(data, 0)


def generate_diff(file1, file2, formatter=stylish):
    file1, file2 = load_files(file1, file2)
    if not file1 and not file2:
        return "Files types are different or file(s) are empty"
    return formatter(build_diff(file1, file2))


# print(generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json"))
