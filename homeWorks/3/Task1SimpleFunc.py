"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def my_sum(arg_1, arg_2):
    try:
        return round(arg_1 / arg_2, 3)
    except ZeroDivisionError:
        print("Division by zero")
        return


x, y = (input("Введите два числа через пробел:").split())
print(f"Result is ", my_sum(int(x), int(y)))
