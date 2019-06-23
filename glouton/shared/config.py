import os
import json

def read():
    with open('glouton-config.json', 'r') as f:
    #with open(os.path.join(os.path.dirname(__file__), '../config.json'), 'r') as f:
        config = json.load(f)
    return config
