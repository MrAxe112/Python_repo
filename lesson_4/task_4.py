a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for number, el in enumerate(a) if a.count(a[number]) == 1])
