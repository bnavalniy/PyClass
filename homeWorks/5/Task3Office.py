"""

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""
from statistics import mean


def get_workers_from_file(file_name):
    workers = {}
    with open(file_name) as file:
        for line in file:
            (name, salary) = line.split(" ")
            workers[name] = float(salary)
    return workers


def get_low_salary(workers):
    return [worker[0] for worker in workers.items() if worker[1] <= 20000.0]


def get_average(workers):
    return mean(dict(workers).values())


print(get_low_salary(get_workers_from_file("text_3.txt")))
print(get_average(get_workers_from_file("text_3.txt")))
