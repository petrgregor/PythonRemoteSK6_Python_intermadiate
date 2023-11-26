from copy import deepcopy
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
seznam = [1, obdelnik_1, 3]
melka_kopie_seznamu = list(seznam)
hluboka_kopie_seznamu = deepcopy(seznam)
seznam[0] = 55  # Změníme hodnotu seznamu
seznam[1].a = 5  # Změníme hodnotu strany obdélníku
print(f"Původní seznam: {seznam}")
print(f"Mělká kopie seznamu: {melka_kopie_seznamu}")
print(f"Hluboká kopie seznamu: {hluboka_kopie_seznamu}")
