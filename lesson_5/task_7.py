from json import dump
company_profit = {}
with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        company_profit[line.split()[0]] = (int(line.split()[2]) - int(line.split()[3]))

avg_profit = sum([int(num) for num in company_profit.values() if num > 0]) / len(
    [int(num) for num in company_profit.values() if num > 0])

with open("text_7.json", "w", encoding="utf-8") as jfile:
    dump([company_profit, {"average_profit": avg_profit}], jfile, ensure_ascii=False)
