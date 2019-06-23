import os
import json

def read():
    config = None
    try:
        with open('glouton-config.json', 'r') as f:
        #with open(os.path.join(os.path.dirname(__file__), '../config.json'), 'r') as f:
            config = json.load(f)
    except FileNotFoundError as enfe_err:
        print("error: glouton configuration's file hasn't been found. Copy it from the sources and name it: ./glouton-config.json")
    return config
