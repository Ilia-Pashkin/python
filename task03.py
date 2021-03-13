class UserTypeError(Exception):
    pass


class Number:
    my_list = []

    def user_append(x):
        try:
            if not x.isdigit():
                raise UserTypeError
            else:
                Number.my_list.append(float(x))
        except:
            print("Введено не число")


while True:
    x = input()
    if x == "stop":
        print(Number.my_list)
        break
    Number.user_append(x)
