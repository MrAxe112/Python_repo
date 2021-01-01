with open("text_2.txt", "r", encoding="utf-8") as file:
    for number, el in enumerate(file.readlines(), 1):
        print(f"В строке {number} - {len(el.split())} слов")
