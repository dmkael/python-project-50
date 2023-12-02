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


# Если нужно добавить поддержку чтения по сети,
# то нужна функция-прослойка,
# которая по path_to_file определит тип пути
# и по нему выдаст способ чтения данных.
# Эту функцию-прослойку нужно указать в модуле gendiff.py
# в функции generate_diff для чтения файлов file1 и file2
# вместо текущей read_local_file.
# Т.к. сейчас способ чтения только локально из папки
# то функции-прослойки нет и используется
# прямое чтение файлов через функцию read_local_file.
def read_local_file(path_to_file):
    split_extension = str(path_to_file).split(".")
    file_extension = split_extension[-1]
    with open(path_to_file, 'r') as file_data:
        loaded_file = load_file(file_data, file_extension)
        if loaded_file:
            return loaded_file
        else:
            raise ValueError('Unsupported file type')
