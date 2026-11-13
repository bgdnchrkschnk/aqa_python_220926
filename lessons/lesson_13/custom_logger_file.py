import logging
from pathlib import Path

custom_logger_file = logging.getLogger("custom_logger_console")

custom_logger_file.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(Path(__file__).parent.parent.parent / "custom_logger_file.log")

file_handler.setLevel(logging.DEBUG) # more priority

formatter = logging.Formatter('LOGGER:%(name)s: [%(filename)s] - [%(funcName)s] - [line:%(lineno)d] -%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

custom_logger_file.addHandler(file_handler)

custom_logger_file.info("This is info level log of custom logger")
custom_logger_file.error("This is error level log of custom logger")
custom_logger_file.warning("This is warning level log of custom logger")
custom_logger_file.critical("This is critical level log of custom logger")