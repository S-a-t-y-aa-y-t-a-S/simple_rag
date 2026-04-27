import sys
import logging
from logging.handlers import RotatingFileHandler
from ingestion.utils.helpers import Helper


class Logger:

    def __init__(self, helper: Helper):

        self.__logger_config = helper.get_logger_config()
        self.__root_logger.setLevel(level=logging.DEBUG)
        self.__log_file = self.__logger_config.target_log_file
        self.__logging_formatter = logging.Formatter(
            fmt=self.__logger_config.logging_formatter,
            datefmt=self.__logger_config.datetime_format
        )


    def get_loggers(self):
        if not self.__root_logger.handlers:
            
            console = logging.StreamHandler(stream=sys.stdout)
            file = RotatingFileHandler(filename=self.__log_file)

            for handler in [console, file]:
                handler.setFormatter(fmt=self.__logging_formatter)
                self.__root_logger.addHandler(handler)

        return self.__root_logger