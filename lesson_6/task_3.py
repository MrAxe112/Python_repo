class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f"{self.name} {self.surname}")

    def get_total_incom(self):
        return print(self._income.get("wage") + self._income.get("bonus"))


worker_1 = Position('Alex', 'Smith', "Math Teacher", 1000, 200)
worker_1.get_full_name()
worker_1.get_total_incom()

worker_2 = Position('Ivan', 'Orlov', 'manager', 800)
worker_2.get_full_name()
worker_2.get_total_incom()
