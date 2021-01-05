class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_per_cm, road_thickness_cm):
        return print(f'масса асфальта равна {(self._length * self._width * mass_per_cm * road_thickness_cm)/1000} тонн')


road_1 = Road(20, 5000)
road_1.mass(25, 5)
