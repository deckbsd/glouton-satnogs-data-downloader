import json

def read():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config