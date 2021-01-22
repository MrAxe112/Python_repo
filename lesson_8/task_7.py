class Complex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __str__(self):
        return f'{self.real} {self.im}'

    def __add__(self, other):
        return Complex(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.im * other.im, self.im * other.real + self.real * other.im)


a1 = Complex(2, 1)
a2 = Complex(3, 5)
print(a1 + a2)

a3 = Complex (3, 1)
a4 = Complex (2, -3)
print(a3 * a4)
