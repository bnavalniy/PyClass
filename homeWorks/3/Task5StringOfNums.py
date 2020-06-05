"""

5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

"""


def main_func():
    sum_of_all = 0
    while True:
        user_input = [str(i) for i in input("Введите числа через пробел или q для выхода:").split()]
        if 'q' in user_input:
            sum_of_all += exit_sum(user_input)
            print(sum_of_all)
            break
        sum_of_all += my_sum(user_input)
        print(sum_of_all)


def my_sum(user_input):
    try:
        nums = [int(i) for i in user_input]
        return sum(nums)
    except ValueError:
        print(f"Wrong input - {user_input}")


def exit_sum(user_input):
    user_input = list(user_input)
    user_input.remove('q')
    user_input = list(map(int, user_input))
    return sum(user_input)


main_func()
