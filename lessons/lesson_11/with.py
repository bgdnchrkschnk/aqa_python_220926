import time

from types import TracebackType

# file = open("assertt.py", "r")
#
# text_content = file.read()
#
# print(text_content)
#
#
# file.close()

# file = None
# try:
#     file = open("assert.py", "r")
#     text_content: str = file.read()
#     print(text_content)
# except Exception as e:
#     print(f"Something went wrong: {e}")
# finally:
#     if file:
#         file.close()
#         print(f"File is closed: {file.closed}")


# with open("assert.py", "r") as file: # finally block .close()
#     text_content: str = file.read()
#     print(text_content)

# with db.connect(**config) as connection:
#     cursor = connection.cursor()


# open() -> Open() -> instance
# __enter__ -> init file
# __exit__ -> file.close()

class Timer:
    def __enter__(self):
        self.start = time.time()
        print(f"Timer started. Time is: {self.start}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start
        print(duration)


with Timer() as timer: # self.start = time.time()
    time.sleep(7)
