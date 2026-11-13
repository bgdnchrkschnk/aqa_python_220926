from lessons.lesson_13.custom_logger import custom_logger


def assert_logged(condition: bool, msg: str =None, exception: BaseException = AssertionError):
    if not condition:
        custom_logger.error(msg)
        raise exception(msg)