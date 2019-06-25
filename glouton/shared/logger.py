import logging
from glouton.shared import config


class Logger:
    def __init__(self) -> None:
        if config is not None:
            self.__config = _config = config.read()
        if self.__config is not None:
            logging.basicConfig(filename=self.__config['LOGFILE'],
                                format='%(asctime)s %(levelname)s:%(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p',
                                level=logging.DEBUG)

    def Info(self, info) -> None:
        print(info)
        logging.info(info)

    def Error(self, error) -> None:
        print(error)
        logging.error(error)

    def Debug(self, str) -> None:
        print(str)
        logging.debug(str)

    def Warning(self, warning) -> None:
        print(warning)
        logging.warning(warning)

logger = Logger()
