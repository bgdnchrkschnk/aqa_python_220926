# for number in range(1, 11):
#     print(number)

l = ["asd", None, 10.8, True]
my_string = "Hello, World!"

# for item in l:
#     print(f"The item {item}, type: {type(item)}")

# for char in my_string:
#     print(char)


transactions_data: list[dict] = [
    {
        "tran_id": 26772,
        "amount": 120.50,
        "user_id": 30,
        "status": "completed"
    },
    {
        "tran_id": 26773,
        "amount": 40.50,
        "user_id": 22,
    },
    {
        "tran_id": 26771,
        "amount":  0.50,
        "user_id": -21,
        "status": "failed"
    },
    {
        "tran_id": 26771,
        "amount": 0.50,
        "user_id": 20,
        "status": "suspicious"
    },
    {
        "tran_id": 26781,
        "amount":  90.2,
        "user_id": 20,
        "status": "completed"
    }
]

completed_transactions = []
not_completed_transactions = []
ban_list_users = {21, 80, 13}

for transaction_dict in transactions_data:
    if transaction_dict.get("user_id") in ban_list_users:
        print("User is banned! Skipping transaction...")
        continue

    if transaction_dict.get('amount') < 0:
        print("Negative amount detected! Skipping transaction...")
        continue

    if transaction_dict.get('status') == "suspicious":
        print("Suspicious transaction detected! Processing stopped!")
        break

    if transaction_dict.get('status') == "completed": # if <condition>
        completed_transactions.append(transaction_dict)
    else:
        not_completed_transactions.append(transaction_dict)
    # db_client.save_transaction(transaction_dict)
else: # якщо цикл не обірвався, пройшов по усім елементам
    print("All transactions are processed!")


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in list_of_numbers:
#     if number == 5:
#         continue
#     print(number)


# for number in list_of_numbers:
#     print(number)
#     if number == 5:
#         break

tables: dict = {
    "Стіл 1": ["Анна", "Іван"],
    "Стіл 2": ["Оля", "Петро", "Марія"],
    "Стіл 3": ["Сергій"]
}

for table_number, table_guests in tables.items():
    for table_guest in table_guests:
        print(table_number, table_guest)

