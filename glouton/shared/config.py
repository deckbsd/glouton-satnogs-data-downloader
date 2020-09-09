import os
import sys
import json


def read():
    config = None
    default_config = {
        "DEFAULT": {
            "NETWORK_API_URL": "https://network.satnogs.org/api/",
            "DB_API_URL": "https://db.satnogs.org/api/",
            "DB_API_KEY": "",
            "HTTPS_PROXY": "",
            "HTTP_PROXY": ""
        },
        "MODULES": {
            "FOR_EACH": {
                "ARCHIVE": [],
                "WATERFALL": [],
                "DEMODDATA": [],
                "FRAME": [],
                "FOR_ALL_OBSERVATION": []
            },
            "END": {
                "ARCHIVE": [],
                "WATERFALL": [],
                "DEMODDATA": [],
                "FRAME": [],
                "FOR_ALL_OBSERVATION": []
            }
        },
        "LOGFILE": "glouton.log"
    }
    try:
        if os.path.exists(os.path.dirname(sys.argv[0]) + "/../glouton/config.json"):
            with open(os.path.dirname(sys.argv[0]) + "/../glouton/config.json", 'r') as f:
                config = json.load(f)
        else:
            config = default_config

    except Exception as eee:
        print("error: ", eee)
        config = default_config
    return config
