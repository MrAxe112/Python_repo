from functools import reduce


def mult_def(a, b):
    return a * b


print(reduce(mult_def, [el for el in range(100, 1000+1, 2)]))
