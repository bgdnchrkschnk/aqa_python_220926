
class FileHandler:
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = open(self.filepath, mode) # open object

    def read_text(self) -> str:
        return self.file.read()

    def close_connection(self):
        print(f"Closing {self.filepath} connection")
        self.file.close()

    def __del__(self): # control destruction of objects
        self.close_connection()

# file = open("/Users/milan/PycharmProjects/aqa_python_220926/pyproject.toml", "r") # open object
# text_content = file.read()
# ...
# ... # TypeError
# ...
# file.close()

file: FileHandler = FileHandler("/Users/milan/PycharmProjects/aqa_python_220926/pyproject.toml", "r")
text_content: str = file.read_text()
# del != __del__
