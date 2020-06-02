# 4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слов
my_words = str(input("Enter words split by space: "))
split_list = my_words.split(' ')
for ind, el in enumerate(split_list, 1):
    if len(el) > 10:
        print(f"Word '{el}' is longer then 10 letters - cut version is '{el[:10]}' String number: '{ind}' ")
        continue
    print(f"Word is '{el}' String number: '{ind}' ")
