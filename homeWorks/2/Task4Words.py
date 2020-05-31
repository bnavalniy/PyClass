# 4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слов
my_bytes = str(input("Enter words split by space: "))
split_list = my_bytes.split(' ')
for ind, el in enumerate(split_list, 1):
    print(f"Word is '{el}' String number: '{ind}' ")
