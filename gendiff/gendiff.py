from gendiff.file_loader import load_files
from gendiff.diff_builder import build_diff


def generate_diff(file1, file2, formatter):
    file1, file2 = load_files(file1, file2)
    if not file1 and not file2:
        return "Files types are different or file(s) are empty"
    return formatter(build_diff(file1, file2))
