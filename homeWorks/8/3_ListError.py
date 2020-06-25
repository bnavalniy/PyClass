class OwnError(Exception):
    def __init__(self, msg):
        self.msg = msg


def main_func():
    user_list = []
    while True:
        user_input = input("Введите числа или q для выхода:")
        if 'q' in user_input:
            print("FINISHED")
            break
        try:
            if not user_input.isdigit():
                raise OwnError("Not a number!")
        except OwnError as err:
            print(err)
        else:
            user_list.append(int(user_input))

main_func()
