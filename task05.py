class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки объекта '{self.title}'")

class Pen(Stationery):
    def draw(self):
        print(f"Начинаю писать {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Начинаю чертить {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Начинаю рисовать {self.title}")

portrait = Stationery("портрет")
portrait.draw()

essay = Pen("сочинение")
essay.draw()

graph = Pencil("график")
graph.draw()

plan = Handle("план действий")
plan.draw()