csv_row: str = "id123;Bohdan;AQA;Odesa"

split_row: list[str] = csv_row.split(sep=';')

print(split_row)


text = (' Коли ви кажете "текст", ви напевне маєте на увазі "букви та інші символи на екрані мого комп’ютера". '
        'Але комп’ютери не працюють з символами, вони працюють з бітами та байтами. Будь-який текст який ви бачите насправді зберігається в певному кодуванні. '
        'Говорячи дуже грубо, кодування символів - це бінарне відношення між зображенням символів які ви бачите на екрані, і даними які комп’ютер насправді зберігає в пам’яті та на диску. '
        'Існує багато різноманітних кодувань символів, деякі з них оптимізовані для конкретних мов, наприклад англійської, китайської або української, а інші можуть використовуватись в багатьох мовах.')

list_of_sentences: list[str] = text.split(". ")
list_of_sentences = [sentence + "." for sentence in list_of_sentences]

first_sentence: str = list_of_sentences[0]
first_sentence_words: list[str] = text.split() # split() -> strip() + split(" ")

# print(list_of_sentences)
# print(first_sentence)
print(first_sentence_words)


joined_words: str = " ".join(first_sentence_words)
print(joined_words)

# split - str to list[str]
# join - list[str] to str

my_name: str = "Joseph"
my_age: int = 25
my_friends: list[str] = ["John", "Mary", "Jane"]

my_bio = f"My name is {my_name} and I am {my_age} years old. My friends are {' and '.join(my_friends)}"

print(my_bio)
