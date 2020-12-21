properties = ("Название", "Цена", "Количество", "Ед.")
user_answer, goods, a, analyse, num_counter = '', [], {}, {}, 1
while True:
    if user_answer == "n":
        break
    for b in properties:
        a[b] = input(f'Ввеедите позицию товара {b} :')
    goods.append((num_counter, a))
    num_counter += 1
    user_answer = input("Хотите ли ввести еще один вид товаров? Y/N: ")
print(f'Текушие позиции товаров выглядят следующим образом:\n')
print(goods)

for b in goods:
    for k, v in b[1].items():
        analyse.setdefault(k, []).append(v)

print(f'Позиции товаров по характеристикам:\n')
print(analyse)
