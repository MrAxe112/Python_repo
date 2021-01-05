class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print("Запуск отрисовки маркером.")


Stationery.draw("Текст")
Pen.draw("Текст")
Pencil.draw("Текст")
Handle.draw("Текст")

