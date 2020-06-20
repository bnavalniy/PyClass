from abc import ABC, abstractmethod


class ClothesAbs(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def calc_cloth(self):
        pass

    def __str__(self):
        return str(f"{type(self).__name__}")


class Coat(ClothesAbs):
    @property
    def calc_cloth(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(ClothesAbs):
    @property
    def calc_cloth(self):
        return round(2 * self.h + 0.3, 2)


coat = Coat(3, 5)
print(coat, coat.calc_cloth)

s = Suit(1, 2)
print(s, s.calc_cloth)
