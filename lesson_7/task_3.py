class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number >= other.number:
            return Cell(self.number - other.number)
        print(f'{self.number} меньше чем {other.number}, вычитание невозможно.')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def __str__(self):
        return f'В клетке - {self.number} ячеек'

    def make_order(self, row_len):
        result = ["*" * row_len] * (self.number // row_len)
        result.append("*" * (self.number % row_len))
        print('\n'.join(result))


c_1 = Cell(5)
c_2 = Cell(15)
c_3 = c_2 // c_1
c_4 = c_1 * c_2

print(c_1)
print(Cell(5)-Cell(9))
c_1.make_order(3)
c_3.make_order(1)
c_4.make_order(9)