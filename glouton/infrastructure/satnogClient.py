from glouton.shared import config
import os
import requests


class SatnogClient:
    def __init__(self):
        self.config = config.read()
        self.proxies = self._set_proxy()
        self.header = self._get_authorization_header()

    def _set_proxy(self):
        proxies = None
        if "http_proxy" in os.environ and "https_proxy" in os.environ:
            proxies = {
                'http': os.environ['http_proxy'],
                'https': os.environ['https_proxy']
            }
            return proxies
        if self.config['DEFAULT']['HTTP_PROXY'] != "" or self.config['DEFAULT']['HTTPS_PROXY'] != "":
            proxies = {
                'http': self.config['DEFAULT']['HTTP_PROXY'],
                'https': self.config['DEFAULT']['HTTPS_PROXY']
            }

        return proxies

    def _get_authorization_header(self):
        token = self.config['DEFAULT']['DB_API_KEY']
        return {'Authorization': 'Token ' + token}

    def get(self, url, params=None):
        raise NotImplementedError()

    def get_from_base(self, url, params=None):
        raise NotImplementedError()
