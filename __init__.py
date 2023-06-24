import json, os, sys


APPDATA = os.path.expanduser(os.path.join("~", "AppData"))

def read_json(path):
    with open(path, 'r') as file:
        _data = json.load(file)

    return _data


def write_json(path, data):
    with open(path, 'w') as file:
        file.write(json.dumps(data, indent=4, sort_keys=True))

