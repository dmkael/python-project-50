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
    loader = LOADERS.get(file_extension)
    if not loader:
        raise ValueError('Wrong file')
    with open(path_to_file, 'r') as file:
        loaded_file = loader(file)
        return loaded_file
