from pathlib import Path
from faker import Faker
fake = Faker()

current_dir = Path.cwd()
repository_dir = current_dir.parent.parent

temp_dir = current_dir / "temp"
temp_dir.mkdir(parents=True, exist_ok=True)


filename_w = "temp_written_file_w.txt"
filename_a = "temp_written_file_a.txt"
file_test_logs = "test_logs.log"
file_test_logs_copy = "test_logs_copy.txt"

file_w: Path = temp_dir / filename_w
file_a: Path = temp_dir / filename_a # Filepath
file_test_logs: Path = repository_dir / file_test_logs
file_test_logs_copy: Path = temp_dir / file_test_logs_copy


# ----------------------------------------------------- write with mode "w"

# file = open(file_w, "w")
# file.close()

with file_w.open("w") as file: # __enter__, __exit__
    file.write(fake.text(max_nb_chars=100)) # inputs string
    file.write("\nMy name is Bohdan")
    file.write("\n\\n - symbol for going to new line")

# ----------------------------------------------------- write with mode "a"

with file_a.open("a") as file:
    file.write("\n" + fake.text(max_nb_chars=100))
    file.write("\nMy name is Bohdan")
    file.write("\n\\n - symbol for going to new line")


# ----------------------------------------------------- read with mode "r"

with file_test_logs.open("r") as file:
    all_file_text: str = file.read() # read the whole file
    print(all_file_text)

with file_test_logs.open("r") as file:
    all_file_lines_text: list[str] = file.readlines()
    # for file_line in all_file_lines_text:
    #     print(file_line)


with file_test_logs_copy.open("w") as file:
    # for line in all_file_lines_text:
    #     file.write(all_file_text)
    file.writelines(all_file_lines_text) # inputs collection of strings
