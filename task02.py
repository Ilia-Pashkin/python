from abc import abstractmethod

class Clothes:
    sum = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.v = size
        Clothes.sum += self.v / 6.5 + 0.5

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size):
        self.h = size
        Clothes.sum += 2 * self.h + 0.3

    @property
    def consumption(self):
        return 2 * self.h + 0.3


m = Coat(180)
print(m.consumption)
n = Suit(15)
print(n.consumption)
print(f"Итого: {Clothes.sum}")