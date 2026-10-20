weather_data = {
    "temperature": -5,
    "humidity": 50,
    "is_raining": True
}

# if weather_data['temperature'] < 0: # if condition
#     print("It's freezing! Take on hat!")
# if weather_data['temperature'] < 10:
#     print("It's cold! Take on jacket!")
# if weather_data['temperature'] > 20:
#     print("It's hot! Take on scarf!")
#
# if weather_data['temperature'] < 0:
#     print("It's freezing! Take on hat!")
# else:
#     if weather_data['temperature'] < 10:
#         print("It's cold! Take on jacket!")
#     if weather_data['temperature'] > 20:
#         print("It's hot! Take on scarf!")
#
#
# if weather_data['temperature'] < 0:
#     print("It's freezing! Take on hat!")
# elif weather_data['temperature'] < 10:
#     print("It's cold! Take on jacket!")
# elif weather_data['temperature'] > 20:
#     print("It's hot! Take on scarf!")


age = 13
name = "Jane"
gender = "female"
user_id = 101

vip_list = [101, 102, 205, 563]


# girls >= 18 - 200
# boys >=16 - 500
# vip_list - free


if gender == "male" and age >=16 and user_id not in vip_list:
    entry_price = 500
    print(f"User {name} with id {user_id} is eligible for entry. Price: {entry_price} uah")
elif gender == "female" and age >=18 and user_id not in vip_list:
    entry_price = 200
    print(f"User {name} with id {user_id} is eligible for entry. Price: {entry_price} uah")
else:
    if user_id in vip_list:
        print(f"User {name} with id {user_id} is eligible for entry. Price: free")
    else:
        if gender == "female" and age < 18:
            print(f"Females under 18 years old are not eligible for entry.")
        elif gender == "male" and age < 16:
            print(f"Males under 16 years old are not eligible for entry.")