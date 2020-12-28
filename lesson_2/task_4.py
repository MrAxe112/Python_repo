user_input = input("Введите строку и из нескольких слов: ")

for number, word in enumerate(user_input.split(), 1):
    print(f'{number}. {word[:10]}')
