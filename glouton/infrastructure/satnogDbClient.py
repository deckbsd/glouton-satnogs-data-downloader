from glouton.infrastructure.satnogClient import SatnogClient
import os
import requests


class SatnogDbClient(SatnogClient):
    def __init__(self):
        SatnogClient.__init__(self)
        self._url = self.config['DEFAULT']['DB_API_URL']

    def get(self, url, params=None):
        return requests.get(url, params=params, proxies=self.proxies)

    def get_from_base(self, url, params=None):
        return requests.get(self._url + url, params=params, proxies=self.proxies)
