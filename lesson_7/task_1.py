class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = (len(self.matrix), len(self.matrix[0]))
        return self._size

    def __str__(self):
        prt = "\n".join((str(line) for line in self.matrix))
        return "".join(el.strip(',[]') for el in prt)

    def __add__(self, other):
        if not self.size == other.size:
            raise ValueError("Матрицы разного размера")

        matrix_sum = [[a + b for a, b in zip(line1, line2)] for line1, line2 in zip(self.matrix, other.matrix)]
        return Matrix(matrix_sum)


m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(m_2 + m_1)
