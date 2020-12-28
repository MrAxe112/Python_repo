def divide (number_1, number_2):
    try:
        return float(number_1)/float(number_2)
    except ValueError:
        return "Для работы нужны цифры"
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"


user_number = input("Введите 2 числа: ").split()
print(divide(*user_number))
