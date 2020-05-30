income = float(input("Выручка: "))
expenses = float(input("Издержки: "))
result = income - expenses

if result > 0:
    profit = result
    print(f"Прибыль: {result}")
    print(f"Рентабильность: {round(result / income)}")
    staff = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сотрудника = {round(profit / staff)}")
elif result == 0:
    print(f"Нет убытка и нет прибыли:")
else:
    print(f"Убыток: {result}")
