error_type: str = "ValueError"
error_message: str = "invalid literal for int() with base 10: 'a'"


log_message: str = f"ERROR type: {error_type} ERROR message: {error_message}"
log_message_concatenation: str = "ERROR type: " + error_type + " ERROR message: " + error_message

print(log_message)
print(log_message_concatenation)


print("10" + "15")
print(10 + 15)