from abc import abstractmethod

class Storage:
    max_volume = 200
    number = 0
    volume = 0
    items = {"printer": 0, "scaner": 0, "xerox": 0}

    def __init__(self):
        pass

    def info(self=None):
        print(f"Занято места: {Storage.volume}")
        print(f"Осталось места: {Storage.max_volume - Storage.volume}")
        print(f"Предметов на складе: {Storage.number}")
        print(f"Подробнее: {Storage.items}")

    def buy(self, buy):
        Storage.max_volume += buy


class OrgTech:
    requires = 0
    key = ""

    def __init__(self, number):
        if number.isdigit():
            number = int(number)
            if Storage.volume + number * self.requires > Storage.max_volume:
                print("Недостаточно места")
                print("Для того, чтобы увеличить количество мест, введите: 'buy <количество мест>'")
            else:
                Storage.number += number
                Storage.volume += number * self.requires
                Storage.items[self.key] += number
                print("Предметы добавлены")
        else:
            print("Вы ввели нечисловое значение для количества")


class Printer(OrgTech):
    requires = 1
    key = "printer"


class Scaner(OrgTech):
    requires = 2
    key = "scaner"


class Xerox(OrgTech):
    requires = 3
    key = "xerox"

print("Введите предмет, который хотите добавить на склад и его количество через пробел, например: 'xerox 10'")
print("Для информации о предметах введите 'info'")
print("Для завершения программы, введите 'stop'")

i = 0
while True:
    a = input().lower()
    if a == "stop":
        break
    a = a.split(" ")
    if len(a) == 2:
        if a[0] == "printer":
            Printer(a[1])
        elif a[0] == "scaner":
            Scaner(a[1])
        elif a[0] == "xerox":
            Xerox(a[1])
        elif a[0] == "buy":
            Storage.buy(None, a[1])
    else:
        if a == ["info"]:
            Storage.info()

    if i == 4:
        print("Для завершения программы, введите 'stop'")
        i = 0
        continue
    i += 1