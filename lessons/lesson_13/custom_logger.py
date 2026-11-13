import logging
from pathlib import Path

custom_logger = logging.getLogger("custom_logger")

custom_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(Path(__file__).parent.parent.parent / "test_logs.log")

console_handler.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()

formatter_console = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_file = logging.Formatter('LOGGER:%(name)s: [%(filename)s] - [%(funcName)s] - [line:%(lineno)d] -%(asctime)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_file)

custom_logger.addHandler(console_handler)
custom_logger.addHandler(file_handler)


if __name__ == "__main__":
    custom_logger.info("This is info level log of custom logger (console stream)")
    custom_logger.error("This is error level log of custom logger (console stream)")
    custom_logger.warning("This is warning level log of custom logger (console stream)")
    custom_logger.critical("This is critical level log of custom logger (console stream)")
