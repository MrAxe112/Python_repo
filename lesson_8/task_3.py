class NotANum(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_func():
    main_str = []
    exit_value = True
    while exit_value:
        low_str = input(f"Введит только число без пробелов. Для выхода введите последним stop: ")
        try:
            if low_str.lower() == "stop":
                exit_value = False
                break
            elif not low_str.isdigit():
                raise NotANum(f"Введенная строка {low_str} не число")
            else:
                main_str.append(int(low_str))
                print(f"Текушие значения {main_str}")
        except NotANum as err:
            print(err)
    print(f"Программа завершена. Конечные значения : {main_str}")


my_func()
