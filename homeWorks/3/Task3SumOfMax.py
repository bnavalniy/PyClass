"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

"""


def my_func(x, y, z):
    params = [y, x, z]
    max_1 = params.pop(params.index(max(params)))
    max_2 = params.pop(params.index(max(params)))
    return max_1 + max_2


x, y, z = (input("Введите три числа через пробел:").split())
print(x, y, z)
print(f"Result is ", my_func(int(x), int(y), int(z)))
