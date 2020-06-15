"""

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
One — 1
Two — 2

"""


# Why it's returned - {'One ': 1} instead of {'One': 1}
def translate_to_rus(content):
    eng_line = {}
    rus_line = {}
    lin = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    (key, value) = str(content).strip().split("-")
    eng_line[key] = int(value)
    for el in eng_line.items():
        value = str(el[0]).strip()
        rus_line.update({lin.get(value): el[1]})
    return rus_line


def write_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(str(content) + "\n")


def main_func(read_file_name, write_file_name):
    file = open(read_file_name)
    for line in file:
        rus_content = translate_to_rus(line)
        write_to_file(write_file_name, rus_content)
    file.close()


main_func("text_4.txt", "translated.txt")
