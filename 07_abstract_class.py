from abc import ABC, abstractmethod
from math import pi


class Utvar(ABC):
    @abstractmethod
    def obvod(self):
        pass

    @abstractmethod
    def plocha(self):
        pass


class Obdelnik(Utvar):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obvod(self):
        return 2 * (self.a + self.b)

    def plocha(self):
        return self.a * self.b


class Kruh(Utvar):
    def __init__(self, r):
        self.r = r

    def obvod(self):
        return 2 * self.r * pi

    def plocha(self):
        return pi * self.r ** 2


try:
    utvar = Utvar()  # TypeError: Can't instantiate abstract class Utvar with abstract methods obvod, plocha
except:
    pass
obdelnik = Obdelnik(3, 5)
kruh = Kruh(12)
print(obdelnik.obvod())
print(kruh.obvod())
print(obdelnik)
