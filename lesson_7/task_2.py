from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        self._cloth = None

    @abstractmethod
    def get_cloth(self):
        return self._cloth

    def __str__(self):
        return f'{self.get_cloth()}'

    def __add__(self, other):
        return self.get_cloth + other.get_cloth


class Coat(Clothes):
    def __init__(self, size=0):
        super().__init__()
        self.size = size

    @property
    def get_cloth(self):
        if self._cloth is None:
            self._cloth = (self.size / 6.5) + 0.5
        return self._cloth


class Suit(Clothes):
    def __init__(self, height=0):
        super().__init__()
        self.height = height

    @property
    def get_cloth(self):
        if self._cloth is None:
            self._cloth = (self.height * 2) + 0.3
        return self._cloth


my_coat = Coat(13)
my_suit = Suit(10)

print(my_coat.get_cloth)
print(my_suit.get_cloth)
print(f'Всего на производство уйдет {my_coat + my_suit} ткани')
