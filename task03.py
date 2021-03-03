class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": _income[0], "bonus": _income[1]}

class Position(Worker):
    def get_full_name(self):
        return self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

p1 = Position("Андрей", "Петров", "Senior", [150_000, 30_000])

print(p1.get_full_name())
print(p1.get_total_income())

