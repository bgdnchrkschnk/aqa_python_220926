text_example: str = "Все, що, як вам здається, ви знаєте про текст — неправда. (с) Dive into Python "


encoded_text = text_example.encode(encoding="windows-1251")
decoded_text = encoded_text.decode(encoding="windows-1251")

print(encoded_text, type(encoded_text))
print(decoded_text, type(decoded_text))