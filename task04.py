class Car:
    is_police = False
    is_going = False
    real_speed = 0

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        self.real_speed = self.speed
        print("Машина поехала")
        if self.is_police == True:
            print("Мигалка и сирена включены")

    def stop(self):
        self.real_speed = 0
        print("Машина остановилась")
        if self.is_police == True:
            print("Мигалка и сирена выключены")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость: {self.real_speed}")

    def change_speed(self, speed):
        if self.real_speed < speed:
            print("Машина ускорилась")
        elif self.real_speed > speed:
            print("Машина замедлилась")
        self.real_speed = speed

class TownCar(Car):
    def show_speed(self):
        if self.real_speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Скорость: {self.real_speed}")

class WorkCar(Car):
    def show_speed(self):
        if self.real_speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Скорость: {self.real_speed}")

class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police = True

print("Поездка на спорткаре:")
car1 = SportCar(300, 'red', 'Lamborgini')
car1.show_speed()
car1.go()
car1.show_speed()
car1.stop()
car1.show_speed()
print()

print("Поездка на обычном авто:")
car2 = TownCar(70, 'dark-blue', 'Hyunday')
car2.go()
car2.show_speed()
car2.change_speed(58)
car2.show_speed()
car2.turn("направо")
car2.stop()
print()

print("Поездка на тракторе:")
car3 = WorkCar(40, 'Orange', 'Tractor')
car3.go()
car3.show_speed()
car3.turn("налево")
car3.change_speed(45)
car3.show_speed()
car3.stop()
print()

print("Поездка на полицейской машине:")
car4 = PoliceCar(80, 'White', 'Toyota')
car4.go()
car4.show_speed()
car4.change_speed(120)
car4.show_speed()
car4.turn("направо")
car4.stop()
