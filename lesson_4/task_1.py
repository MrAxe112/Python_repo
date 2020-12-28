from sys import argv


def salary(work_hours, wage, bonus=0):
    return round((float(work_hours) * float(wage)) + float(bonus), 2)


error_msg = 'Для выполнения расчетов необходимо указать, используя числа, через пробел: "Количество отработанных ' \
            'часов" "Ставку зарабатной платы в час" "Премию (если она есть)"'
try:
    args = argv[1:]
    print(salary(*args))
except TypeError:
    print(error_msg)
except ValueError:
    print(error_msg)
