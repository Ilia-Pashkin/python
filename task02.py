class UserZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

class UserMath:
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        try:
            if other.x == 0:
                raise UserZeroDivisionError
            else:
                return self.x / other.x
        except:
            return "Ошибка деления на нуль"

x = UserMath(5)
y = UserMath(0)

print(x / y)