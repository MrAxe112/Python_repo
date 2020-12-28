def my_func(x, y):
    if x > 0 and y < 0:
        return x ** y
    else:
        return "Условия задачи не выполнены! (Положительный X и отрицательный Y)"


numbers = [float(input("Введите действительное положительное число (X): ")),
           int(input("Введите целое отрицательное число (Y): "))
           ]
print(my_func(*numbers))
