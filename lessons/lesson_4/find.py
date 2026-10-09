config_db: str = "host=localhost;port=5432;dbname=test_db_name;user=admin;password=Qwerty123"


port_index = config_db.find("port")
db_name_index = config_db.find("dbname")
user_index = config_db.find("user")
password_index = config_db.find("password")


port_slice = config_db[port_index+5:db_name_index-1]
# print(port_slice)

log_data: str = """
INFO: Service started
CRITICAL: Database connection failed 
WARNING: High memory usage
CRITICAL: Timeout occurred
"""

first_critical = log_data.find("CRITICAL:")
second_critical = log_data.find("CRITICAL:", first_critical+1)

first_msg_index = first_critical + len("CRITICAL: ")
return_first_index = log_data.find("\n", first_msg_index)
second_msg_index = second_critical + len("CRITICAL: ")

first_msg = log_data[first_msg_index: return_first_index]
print(first_msg)



