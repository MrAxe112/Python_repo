user_input = list(input("Введите несколько произвольных букв или цифр: "))
print(user_input)

for a in range(1, len(user_input), 2):
    user_input[a - 1], user_input[a] = user_input[a], user_input[a - 1]

print(user_input)

