def avg(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)


test_data = [
    ([1,2,3,4,5], 3),
    ([5,10,13,26], 13.5),
    ([-43, 12, 0, 7], -6)
]


for list_of_numbers, expected_result in test_data:
    assert avg(list_of_numbers) == expected_result, f"List_of_numbers {list_of_numbers} AVG: \nExpected {expected_result}, but got {avg(list_of_numbers)}"




# assert <bool_condition> # AssertionError

assert True
# assert False

# assert 5+5 == 11 or 6+7 == 12, f"this is not True" # True or False -> True


# if not (5+5 == 11 or 6+7 == 12):
#     raise AssertionError("this is not True")

ban_transactions = [55, 64, 80, 22, 67]

pending_transactions = list(range(1, 100))

# for pending_transaction in pending_transactions:
#     # if pending_transaction in ban_transactions:
#     #     raise AssertionError("transaction is banned. stopping process")
#     assert pending_transaction not in ban_transactions, f"transaction {pending_transaction} not in banned transactions"
#     print(pending_transaction)
