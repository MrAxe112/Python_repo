def my_func(number_1, number_2, number_3):
    try:
        list_of_numbers = int(number_1), int(number_2), int(number_3)
        return sum(sorted(list_of_numbers)[1:])
    except ValueError:
        return "Для работы программы необходимы только числа!"


user_numbers = input("Введите 3 числа: ").split()
print(my_func(*user_numbers))
