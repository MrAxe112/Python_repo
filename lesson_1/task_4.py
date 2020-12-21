
# Пользователь вводит целое положительное число
number = int(input("Введите целое положительное число: "))

# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции
a = number % 10
number = number // 10

while number > 0:
    if number % 10 > a:
        a = number % 10
    number = number // 10

print(a)
