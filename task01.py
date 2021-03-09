class Matrix:

    def __init__(self, a):
        self.matrix = []
        for i in range(len(a)):
            self.matrix.append([])
            for j in range(len(a[0])):
                self.matrix[i].append(a[i][j])

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        C = []
        for i in range(len(self.matrix)):
            C.append([])
            for j in range(len(self.matrix[0])):
                C[i].append(self.matrix[i][j] + other.matrix[i][j])
        return C


A = Matrix([[1, 0, 2], [0, 1, 2]])
B = Matrix([[0, 1, 2], [1, 0, 2]])
print(A + B)
