class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, date):
        d, m, y = date.split("-")
        return cls(int(d), int(m), int(y))

    @staticmethod
    def val(cl):
        if 1 <= cl.day <= 31 :
            print("День корректен")
        else:
            print("День некорректен - должно быть число от 31")

        if 1 <= cl.month <= 12:
            print("Месяц корректен")
        else:
            print("Месяц некорректен - должно быть число от 1 по 12")

        if 1 <= cl.year <= 2099:
            print("Год корректен")
        else:
            print("Год некорректен - должно быть число от 1 по 2099")

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"


yer = Date.get_date("12-11-2012")
print(yer)
Date.val(yer)
