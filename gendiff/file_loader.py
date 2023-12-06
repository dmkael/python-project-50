import json
import yaml


LOADERS = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load
}


def load_data(file_data, extension):
    loader = LOADERS.get(extension)
    if not loader:
        raise ValueError('Unsupported file type')
    loaded_data = loader(file_data)
    if not isinstance(loaded_data, dict):
        raise ValueError("Wrong data in file")
    return loaded_data


def read_local_file(path_to_file):
    split_extension = str(path_to_file).split(".")
    file_extension = split_extension[-1]
    with open(path_to_file, 'r') as file:
        file_data = file.read()
        return load_data(file_data, file_extension)
