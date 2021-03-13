class ComplexNumber:
    def __init__(self, x):
        self.a = x[0]
        self.b = x[1]

    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return((self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a))

    def __pow__(self, power, modulo=None):
        result = (self.a, self.b)
        for i in range(power - 1):
            result = (self.a * result[0] - self.b * result[1], self.a * result[1] + self.b * result[0])
        return result

x = ComplexNumber((5, -1))
y = ComplexNumber((-1, 5))
print(x + y)
print(x * y)

i = ComplexNumber((0, 1))
print(i ** 2)
print(i ** 4)