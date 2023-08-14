import json, os, sys, pathlib


APPDATA = os.path.expanduser(os.path.join("~", "AppData"))

def read_json(path):
    with open(path, 'r') as file:
        _data = json.load(file)

    return _data


def write_json(path, data):
    with open(path, 'w') as file:
        file.write(json.dumps(data, indent=4, sort_keys=True))


def get_filepath_with_suffix(filepath, suffix):
    _path = pathlib.Path(filepath)
    _path_dir = _path.parent
    _path_name = _path.stem
    _path_suffix = _path.suffix

    _name = f"{str(_path_name)}{suffix}{_path_suffix}"

    _path = os.path.join(str(_path_dir), _name)

    return _path

def add_suffix_to_filepath(filepath, suffix):

    _path = get_filepath_with_suffix(filepath, suffix)

    if os.path.exists(_path):
        while os.path.exists(_path):
            _path = add_suffix_to_filepath(_path)

    os.renames(filepath, _path)

    return _path



if __name__ == "__main__":
    _p = r"C:\Users\Tanner - Work\Documents\Settings\queues.json"

    print(add_suffix_to_filepath(_p, "suffix"))
