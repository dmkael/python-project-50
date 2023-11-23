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
        with open(path_to_file, 'r') as file:
            loaded_file = LOADERS.get(file_extension)(file)
            return loaded_file
    print(f"'.{file_extension}' is not supported file type")
