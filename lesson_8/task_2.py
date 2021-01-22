class DevByZr(Exception):
    def __init__(self, txt):
        self.txt = txt


num = int(input("Введите число для деления на число 100: "))

try:
    if num == 0:
        raise DevByZr("Делить на 0 нельзя !!!")
    else:
        print(100 / num)
except DevByZr as err:
    print(err)
