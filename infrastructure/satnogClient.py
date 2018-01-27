from shared import config
import os
import requests


class SatnogClient:
    def __init__(self):
        self._config = _config = config.read()
        self._url = _config['DEFAULT']['API_URL']
        self._proxies = self._set_proxy()

    def _set_proxy(self):
        proxies = None
        if "http_proxy" in os.environ and "https_proxy" in os.environ:
            proxies = {
                'http': os.environ['http_proxy'],
                'https': os.environ['https_proxy']
            }
            return proxies
        if self._config['DEFAULT']['HTTP_PROXY'] != "" or self._config['DEFAULT']['HTTPS_PROXY'] != "":
            proxies = {
                'http': self._config['DEFAULT']['HTTP_PROXY'],
                'https': self._config['DEFAULT']['HTTPS_PROXY']
            }

        return proxies

    def get(self, url, params=None):
        return requests.get(url, params=params, proxies=self._proxies)

    def get_from_base(self, url, params=None):
        return requests.get(self._url + url, params=params, proxies=self._proxies)
