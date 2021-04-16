import os
import mock
import pytest
import requests
from glouton.infrastructure.satnogNetworkClient import SatnogNetworkClient
from glouton.infrastructure.satnogDbClient import SatnogDbClient


@mock.patch.dict(os.environ, {"SATNOGS_NETWORK_API_URL": "network_url_from_env"})
def test_network_api_url_via_env_variable():
    with pytest.raises(requests.exceptions.MissingSchema) as ex:
        client = SatnogNetworkClient()
        client.get_from_base("/test")
    assert "network_url_from_env/test" in str(ex.value)


@mock.patch.dict(os.environ, {"SATNOGS_DB_API_URL": "db_url_from_env"})
def test_db_api_url_via_env_variable():
    with pytest.raises(requests.exceptions.MissingSchema) as ex:
        client = SatnogDbClient()
        client.get_from_base("/test")
    assert "db_url_from_env/test" in str(ex.value)
