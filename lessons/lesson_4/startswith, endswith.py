filename = "server_output.log"
fake_csv_filename = "fake_datacsv"

is_log_file: bool = filename.endswith(".log")
is_csv_file: bool = fake_csv_filename.endswith(".csv")

print(is_log_file)
print(is_csv_file)


log_message = "INFO: request was proceed. Redirected to next step"
log_message_2 = "ERROR: invalid literal for int() with base 10: 'a'"

is_log_critical_error: bool = log_message_2.startswith("ERROR")

print(is_log_critical_error)

# if log_message_2.startswith("ERROR"):
#     print("Stopping the program")

if is_log_critical_error:
    print("Stopping the program")