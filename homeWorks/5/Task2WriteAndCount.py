"""

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке

"""


def get_file_and_write(file_name):
    with open(file_name, "a") as my_file:
        while True:
            user_input = input("Write to file: ")
            if len(user_input) == 0:
                break
            my_file.writelines("\n" + user_input)


def get_file_read_and_count(file_name):
    with open(file_name) as file:
        list_of_lines = file.readlines()
    list_of_lines_split_by_words = [list(el.split(" ")) for el in list_of_lines if el != '\n']
    for ind, line in enumerate(list_of_lines_split_by_words):
        print(f"Line {ind} - has worlds: {len(line)}")


get_file_and_write("text.txt")
get_file_read_and_count("text.txt")
