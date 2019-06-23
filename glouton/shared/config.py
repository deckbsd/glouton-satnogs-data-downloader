import os
import json

def read():
    config = None
    default_config = {
                "DEFAULT": {
                    "API_URL": "https://network.satnogs.org/api/",
                    "HTTPS_PROXY": "",
                    "HTTP_PROXY": ""
                },
                "MODULES": {
                    "PAYLOAD": [],
                    "WATERFALL": [],
                    "DEMODDATA": [],
                    "FORALL": []
                },
                "LOGFILE": "glouton.log"
            }
    try:
        if os.path.exists("glouton-config.json"):
            with open('glouton-config.json', 'r') as f:
                config = json.load(f)
        else:
            config = default_config

    except Exception as eee:
        print("error: ", eee)
        config = default_config
    return config
