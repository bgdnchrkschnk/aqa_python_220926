filename = "    /var/usrbin/logs/test_log.log/        "

#     filename.strip() # remove all spaces from left, right side
# )
#
# print(
#     filename.lstrip() # remove all spaces from left side
# )
#
# print(
#     filename.rstrip() # remove all spaces from right side
# )

filename = "||||||||||||||||/var/usrbin/logs/test_log.log/|||||||||||||||||"


stripped_filename = filename.strip("|")
print(stripped_filename)

