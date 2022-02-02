import logging
import os


def get_logger(name):
    log_file = os.path.dirname(os.path.realpath(__file__)) + "/app_log.txt"
    level = logging.DEBUG

    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
