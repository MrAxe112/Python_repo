def int_func(arg):
    if arg.isascii() and arg.islower():
        return arg.title()
    else:
        return "Для работы программы необходимо слово или несколько слов из маленьких латинских букв."


print(int_func(input("Введите слово или строку состоящие из маленьких латинских букв: ")))
