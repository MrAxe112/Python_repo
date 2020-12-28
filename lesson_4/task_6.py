from itertools import count, cycle


def num_count(start, break_line=99):
    for el in count(start):
        if el > break_line:
            break
        else:
            print(el)


def repeat_cycle(elem, brake_line=30):
    for num, el in enumerate(cycle(elem)):
        print(el)
        if num > brake_line:
            break


num_count(int(input("Введите число для демонстрации скрипта 1: ")))
repeat_cycle("predetermined")
