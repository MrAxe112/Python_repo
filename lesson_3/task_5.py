def my_func():
    main_result = 0
    exit_value = True
    while exit_value:
        number = input("Введит числа через пробел. Для выхода введите последним q: ").split()
        sub_result = 0
        for a in number:
            if a.lower() == "q":
                exit_value = False
                break
            else:
                sub_result += int(a)
        main_result += sub_result
        print(f'Сумма строки равна {sub_result}, общая {main_result}')


my_func()
