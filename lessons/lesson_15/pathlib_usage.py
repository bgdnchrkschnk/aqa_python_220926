from pathlib import Path

# current_dir = Path.cwd()

# lesson_15_: Path = Path("/Users/milan/PycharmProjects/aqa_python_220926/lessons/lesson_15")


current_dir: Path = Path.cwd() # pwd
home_dir: Path = Path.home()
repository_dir: Path = current_dir.parent.parent # .parent (cd ..)

name_of_repository = repository_dir.name

list_of_repository_obj = list(repository_dir.iterdir())

# for obj in repository_dir.iterdir():
#     if obj.is_dir():
#         print(f"Directory {obj}")
#     elif obj.is_file():
#         print(f"File {obj}")


repository_dirs: list[Path] = [obj for obj in repository_dir.iterdir() if obj.is_dir()]
repository_files: list[Path] = [obj for obj in repository_dir.iterdir() if obj.is_file()]

lesson_13: Path = repository_dir / "lessons" / "lesson_13"

test_logs_13 = lesson_13 / "test_logs" / "inner_logs"
test_log = current_dir / "test_log.log"

test_logs_13.mkdir(parents=True, exist_ok=True) # create directories
test_log.touch() # create files


lesson_15_py_files: list[Path] = [obj for obj in current_dir.iterdir() if obj.is_file() and obj.suffix == ".py"]

