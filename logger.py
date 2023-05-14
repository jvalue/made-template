
import logging
from logging import handlers
import sys
import os
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent

FORMATTER = logging.Formatter(
    "%(asctime)s — %(levelname)s — %(name)s — %(funcName)s:%(lineno)d — %(message)s"
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(file_name):
    file_handler = logging.handlers.TimedRotatingFileHandler(
        os.getcwd() + f"/{file_name}.log")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_socket_handler():
    socket_handler = handlers.SocketHandler(host='localhost', port=9999)
    socket_handler.setFormatter(FORMATTER)
    return socket_handler


def get_file_logger(logger_name, file_name):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler(file_name))
    logger.propagate = False

    return logger
