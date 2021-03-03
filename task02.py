class Road:
    mass_1_sq_m = 0.025
    thickness = 0.05

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        print(f"Потребуется {self._length * self._width * self.mass_1_sq_m * self.thickness}т асфальта")

road1 = Road(1500, 20)
road1.mass()