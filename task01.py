from time import sleep
from itertools import cycle

class TrafficLight:
    state = range(18)
    def __init__(self, time):
        self.time = time

    def running(self):
        t = 0
        for i in cycle(self.state):
            t += 1
            if t > self.time:
                break
            print(f"{i + 1} сек - ", end='')
            if i < 7:
                __color = "красный"
            elif i < 9:
                __color = "желтый"
            else:
                __color = "зеленый"
            print(__color)
            sleep(0.5) #для ускорения

t = TrafficLight(100)
t.running()
