class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} едет")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текушая скорость равна {self.speed} км/ч.")


class TownCar(Car):
    allowed_speed = 60

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed < TownCar.allowed_speed:
            print(f"Текушая скорость равна {self.speed} км/ч.")
        else:
            print(f"Текушая скорость равна {self.speed} км/ч."
                  f" Превышина допустимая скорость {TownCar.allowed_speed} км/ч!")


class SportCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)


class WorkCar(Car):
    allowed_speed = 40

    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if self.speed < WorkCar.allowed_speed:
            print(f"Текушая скорость равна {self.speed} км/ч.")
        else:
            print(f"Текушая скорость равна {self.speed} км/ч."
                  f" Превышина допустимая скорость {WorkCar.allowed_speed} км/ч!")


class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police=True):
        super().__init__(speed, colour, name, is_police)


town_niva = TownCar(50, "Черная", "Нива")
town_niva.turn("назад")
town_niva.show_speed()

work_lada = WorkCar(50, "Белая", "Лада")
work_lada.show_speed()
