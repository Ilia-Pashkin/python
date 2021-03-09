class Cell:
    def __init__(self, sub_cells):
        self.sub_cells = sub_cells

    def __add__(self, other):
        return Cell(self.sub_cells + other.sub_cells)

    def __sub__(self, other):
        if self.sub_cells > other.sub_cells:
            return Cell(self.sub_cells - other.sub_cells)
        else:
            return "У первой клетки должно быть больше ячеек, чем у второй"

    def __mul__(self, other):
        return Cell(self.sub_cells * other.sub_cells)

    def __truediv__(self, other):
        return Cell(self.sub_cells // other.sub_cells)

    def make_order(self, row):
        ordered = ['*']
        for i in range(1, self.sub_cells):
            if i % row == 0:
                ordered.append('\n')
            ordered.append('*')

        return ''.join(ordered)

print("Сложение")
cell1 = Cell(8)
cell2 = Cell(4)
cell3 = cell1 + cell2
print(cell3.make_order(5))
print()

print("Неправильное вычитание:")
print(cell2 - cell1)
print()

print("Правильное вычитание:")
cell3 = cell1 - cell2
print(cell3.make_order(5))
print()

print("Деление:")
cell3 = cell1 / cell2
print(cell3.make_order(5))
print()

print("Произведение:")
cell3 = cell1 * cell2
print(cell3.make_order(8))
