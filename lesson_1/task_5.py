
# Запросите у пользователя значения выручки и издержек фирмы
profit = float(input("Введите значения выручки: "))
costs = float(input("Введите значение издержек: "))

# Определите, с каким финансовым результатом работает фирма
result = profit - costs

# Если фирма отработала с прибылью, вычислите рентабельность выручки
# Выведите соответствующее сообщение
if result <= 0:
    print("Ваша фирма работает в убыток")
elif result > 0:
    print("Ваша фирма работает с прибылью")
    profitability = result/profit
    print(f"Рентабельность выручки равна: {profitability:.2f}")

# Далее запросите численность сотрудников фирмы
employees = int(input("Введите численность сотрудников: "))

# и определите прибыль фирмы в расчете на одного сотрудника
employees_profit = result/employees
print(f"Прыбыль на одного сотрудника состовляет: {employees_profit:.2f}")