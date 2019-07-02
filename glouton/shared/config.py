import os
import json

def read():
    config = None
    default_config = {
                "DEFAULT": {
                    "NETWORK_API_URL": "https://network.satnogs.org/api/",
                    "DB_API_URL": "https://db.satnogs.org/api/",
                    "HTTPS_PROXY": "",
                    "HTTP_PROXY": ""
                },
                "MODULES": {
                    "PAYLOAD": [],
                    "WATERFALL": [],
                    "DEMODDATA": [],
                    "FRAME": [],
                    "FORALL": []
                },
                "LOGFILE": "glouton.log"
            }
    try:
        if os.path.exists(os.getcwd() + "/../glouton/config.json"):
            with open(os.getcwd() + "/../glouton/config.json", 'r') as f:
                config = json.load(f)
        else:
            config = default_config

    except Exception as eee:
        print("error: ", eee)
        config = default_config
    return config
