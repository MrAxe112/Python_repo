from random import sample

random_numbers = sample(range(1, 101), 10)
print(f'Сумма чисел {" ".join(map(str, random_numbers))}\nравна - {sum(random_numbers)}')

with open("text_5.txt", "w", encoding="utf-8") as file:
    file.write(f'{" ".join(map(str, random_numbers))}\nСумма чисел равна - {sum(random_numbers)}')
