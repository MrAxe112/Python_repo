my_list = [7, 5, 3, 3, 2]
end = 999999

while True:
    user_input = int(input("Введите число, новый элемент 'Рейтинга'(вводе числа 999999 завершит сбор информации): "))
    if user_input == end:
        print(my_list)
        break
    elif user_input != end:
        for a in my_list:
            if user_input > a:
                b = my_list.index(a)
                my_list.insert(b, user_input)
                break
            elif my_list.count(user_input) > 0:
                c, d = my_list.index(user_input), my_list.count(user_input)
                my_list.insert(c + d, user_input)
                break
            elif user_input < my_list[len(my_list) - 1]:
                my_list.append(user_input)
                break
    print(my_list)
