"""

6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой.Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

"""


def int_func(user_input):
    ui = list(user_input)
    for i in ui:
        if ord(i) in range(97, 122):
            return str(user_input).capitalize()
    return str(f"Wrong input: {user_input}")


def proceed_func():
    ui = list(input("Введите str через пробел:").split())
    result = []
    for i in ui:
        result.append(int_func(i))
    return result


user_input = input("Enter word with small letters:")
print(int_func(user_input))
print(proceed_func())
