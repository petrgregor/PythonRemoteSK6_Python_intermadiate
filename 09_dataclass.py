from dataclasses import dataclass
from abc import ABC, abstractmethod
from math import pi


class Utvar(ABC):
    @abstractmethod
    def obvod(self):
        pass

    @abstractmethod
    def plocha(self):
        pass

@dataclass
class Obdelnik(Utvar):
    a: int
    b: int

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Obdelnik se stranami a={self.a} a b={self.b}"

    def obvod(self):
        return 2 * (self.a + self.b)

    def plocha(self):
        return self.a * self.b


obdelnik_1 = Obdelnik(3, 4)
obdelnik_2 = Obdelnik(3, 4)
print(obdelnik_1)
print(obdelnik_1 == obdelnik_2)
