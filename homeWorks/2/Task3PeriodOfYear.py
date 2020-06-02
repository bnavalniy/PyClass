# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
input_month = int(input("Enter month number 1-12: "))
periods = dict(spring=[3, 4, 5],
               summer=[6, 7, 8],
               autumn=[9, 10, 11],
               winter=[12, 1, 2])
for period, month in periods.items():
    if input_month in month:
        print(f"Now is {period}")
        break
