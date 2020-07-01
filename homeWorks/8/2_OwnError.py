class OwnError(Exception):
    def __init__(self, msg):
        self.message = msg


inp_data = input("Введите делитель и делимое через пробел: ")

try:
    delimoe, delitel = str(inp_data).split(' ')
    if int(delitel) == 0:
        raise OwnError("На ноль делить нельзя!")
    res = int(delimoe) / int(delitel)
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат: {round(res, 2)}")
finally:
    print("END")
