with open("text_1.txt", "w", encoding="utf-8") as file:
    while True:
        user_input = input(f'Введите строку для добавления в файл {file.name}: ')
        if user_input:
            file.write(f'{user_input}\n')
        else:
            break
