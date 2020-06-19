import mock
from glouton.shared.config import read

default_config = {
                "DEFAULT": {
                    "NETWORK_API_URL": "https://network.satnogs.org/api/",
                    "DB_API_URL": "https://db.satnogs.org/api/",
                    "DB_API_KEY": "",
                    "HTTPS_PROXY": "",
                    "HTTP_PROXY": ""
                },
                "MODULES": {
                    "ARCHIVE": [],
                    "WATERFALL": [],
                    "DEMODDATA": [],
                    "FRAME": [],
                    "FOR_ALL_OBSERVATION": []
                },
                "LOGFILE": "glouton.log"
            }

def exist_return_false():
    return False

def test_default_configuration():
    patcher = mock.patch('os.path.exists')
    exists_mock = patcher.start()
    exists_mock.side_effect = exist_return_false
    config_obj = read()

    assert config_obj == default_config