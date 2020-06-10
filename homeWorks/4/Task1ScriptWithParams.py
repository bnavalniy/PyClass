"""

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv

scr_name, worked_hours, pay_per_hour, bonus = argv


def salary():
    try:
        sal = (int(worked_hours) * int(pay_per_hour)) + int(bonus)
        return sal
    except ValueError:
        return f"Wrong params{argv}"


print(salary())
