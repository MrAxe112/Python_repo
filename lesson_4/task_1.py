def salary(work_hours, wage, bonus=0):
    try:
        return round((float(work_hours) * float(wage)) + float(bonus), 2)
    except TypeError:
        return "Для выполнения необходимо указать количество часов, ставку зарабатной платы и премию (если она есть)."


try:
    from sys import argv
    args = argv[1:]
    print(salary(*args))
except TypeError:
    print('Для выполнения расчетов необходимо указать через пробел: "Количество отработанных часов" '
          ' "Ставку зарабатной платы в час" "Премию"(если она есть).')
