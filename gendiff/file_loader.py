import json
import yaml

LOADERS = {
    "json": json.load,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load
}


def load_file(data, extension):
    loader = LOADERS.get(extension)
    if loader:
        return loader(data)
    else:
        raise ValueError('Unsupported file type')


def read_local_file(path_to_file):
    split_extension = str(path_to_file).split(".")
    file_extension = split_extension[-1]
    with open(path_to_file, 'r') as file_data:
        loaded_file = load_file(file_data, file_extension)
        if loaded_file:
            return loaded_file
        else:
            raise ValueError('Unsupported file type')
