import logging

custom_logger_console = logging.getLogger("custom_logger_console")

custom_logger_console.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.DEBUG) # more priority

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

custom_logger_console.addHandler(console_handler)

custom_logger_console.info("This is info level log of custom logger (console stream)")
custom_logger_console.error("This is error level log of custom logger (console stream)")
custom_logger_console.warning("This is warning level log of custom logger (console stream)")
custom_logger_console.critical("This is critical level log of custom logger (console stream)")