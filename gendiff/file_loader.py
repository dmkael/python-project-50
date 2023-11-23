import json
import yaml

LOADERS = {
    "json": json.load,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load
}


def load_file(path_to_file):
    split_extension = path_to_file.split(".")
    file_extension = split_extension[-1]
    if LOADERS.get(file_extension):
        file = LOADERS.get(file_extension)(open(path_to_file))
        return file
    print(f"'.{file_extension}' is not supported file type")
