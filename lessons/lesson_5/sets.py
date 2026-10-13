set_of_random_values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2}
print(id(set_of_random_values))
empty_set: set = set()

# немає дублікатів
print(set_of_random_values)
# немає порядку індексів

# print(set_of_random_values[0]) # no indexation, no slices

# .add()
set_of_random_values.add(11)
set_of_random_values.add(12)
set_of_random_values.add(1)
print(set_of_random_values)
print(id(set_of_random_values))

set_of_random_data = {"Bohdan", 29, 36.6, True, False, None, (1,2,3)} # only immutable data
print(set_of_random_data)

for item in set_of_random_data:
    print(item)

transactions_ids: list = [1232, 57373, 78934, 2654356, 57373, 37683, 2222]
set_of_transactions_ids: set = set(transactions_ids)


# for transaction_id in set_of_transactions_ids:
#     scheduler_status_check(transaction_id)



expected_result = ["bhjc", "bhjca", "jnwef", "nkajcwef156"]

actual_result = ["bhjc", "bhjca", "jnwef", "nkajcwef156", "jnwef", "nkajcwef156"]


# is_equal_data: bool = len(set(expected_result)) == len(set(actual_result))
is_equal_len_data = len(set(actual_result)) == len(expected_result)
is_equal_data = set(actual_result) == set(expected_result)
print(is_equal_data)

# ----------------------------------------- .update()

set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4, 5, 6}

my_set_3 = set_1 | set_2
print(my_set_3)

set_1.update(set_2)
print(set_1)

# ----------------------------------------- .pop() remove random element


removed_element = set_1.pop()
print(removed_element)

# ----------------------------------------- .remove() remove element by value


set_1.remove(6)
print(set_1)


set_of_tran_ids = {1,2,3,4,5,6,7,8,9,10}

processed_transaction_ids = set()


for tran_id in set_of_tran_ids:
    # email_sender.send_email(tran_id)
    processed_transaction_ids.add(tran_id)


first_set = {1, 2, 3, 4, 5}
second_set = {3, 4, 5, 6, 7}


# difference
difference_set_first = first_set - second_set
difference_set = first_set.difference(second_set)
print(difference_set)


first_set.intersection(second_set) # INNER JOIN

print(
    first_set.intersection(second_set)
)

first_set = {1, 2, 3, 4, 5}
second_set = {3, 4, 5}

print(
    second_set.issubset(first_set)
)


