"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
- Функция должна принимать параметры как именованные аргументы.
- Реализовать вывод данных о пользователе одной строкой."""


def name_params_func(name, surname, year_of_birth, city, email, phone):
    return dict(name=name, surname=surname, year_of_birth=year_of_birth, city=city, email=email, phone=phone)


input_list = [str(i) for i in
              input(" Введите параметры разд запятой: name, surname, year_of_birth, city, email, phone - ").split(
                  ",")]

print(name_params_func(name=input_list[0], surname=input_list[1], year_of_birth=input_list[2], city=input_list[3],
                       email=input_list[4], phone=input_list[5]))
