"""

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""


def write_to_file(file_name):
    file = open(file_name, "w")
    while True:
        user_input = input("Write to file: ")
        if len(user_input) == 0:
            break
        file.writelines(user_input + "\n")
    file.close()


def read_and_write_sum_to_file(file_name_to_read):
    list_of_nums = []
    with open(file_name_to_read, "r+") as file:
        list_of_nums = [int(x) for x in file.readline().split()]
        assert len(list_of_nums) != 0
        file.write(str(sum(list_of_nums)))


write_to_file("nums.txt")
read_and_write_sum_to_file("nums.txt")
