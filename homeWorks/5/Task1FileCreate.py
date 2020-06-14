"""

Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""


def write_to_file(file_name):
    file = open(file_name, "w")
    while True:
        user_input = input("Write to file: ")
        if len(user_input) == 0:
            break
        file.writelines(user_input + "\n")
    file.close()


write_to_file("text.txt")
