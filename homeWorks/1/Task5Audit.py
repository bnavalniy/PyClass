income = float(input("Выручка: "))
expenses = float(input("Издержки: "))
result = income - expenses

if result > 0:
    profit = result
    print(f"Прибыль: {result}")
    print(f"Рентабильность: {result / income}")
elif result == 0:
    print(f"Нет убытка и нет прибыли:")
else:
    print(f"Убыток: {result}")
staff = int(input("Введите количество сотрудников: "))
print(f"Прибыль на одного сотрудника = {profit / staff}")
