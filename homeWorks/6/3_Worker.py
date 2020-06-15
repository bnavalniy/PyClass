"""

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": list(income).pop(0), "bonus": list(income).pop(1)}

    def return_income(self):
        return self._income


class Position(Worker):

    def get_full_name(self):
        return print(f"Name: {self.name} \nSurname: {self.surname}")

    def get_total_income(self):
        income = self.return_income()
        income = dict(income).get("wage") + dict(income).get("bonus")
        return print(f"Income: {income}")


p = Position("Ben", "Stivenson", "QA", [1000, 200])

p.get_full_name()
p.get_total_income()
