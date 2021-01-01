company_data = {}
low_cost = []
with open("text_3.txt", "r", encoding="utf-8") as file:
    for line in file:
        company_data[line.split()[0]] = float(line.split()[1])

for person, salary in company_data.items():
    if salary < 20000:
        low_cost.append(person)
avg_salary = sum(company_data.values())/len(company_data)

print(f"Сотрудники {low_cost} зарабатывают меньше 20 000\n"
      f"На предприятии средняя зарплата составляет - {avg_salary:.2f}")
