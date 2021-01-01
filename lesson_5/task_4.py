dic = {"One": "Один",
       "Two": "Два",
       "Three": "Три",
       "Four": "Четыре"}


with open("text_4(new).txt", "w", encoding="utf-8") as file_2:
    with open("text_4.txt", "r", encoding="utf-8") as file_1:
        file_2.writelines([line.replace(line.split()[0], dic.get(line.split()[0])) for line in file_1])
