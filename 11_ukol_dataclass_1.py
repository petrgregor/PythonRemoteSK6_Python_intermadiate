"""
Úkol 1

Vytvořte třídu pojmenovanou Tester jako datovou třídu (dataclass), která:

    bude mít v konstruktoru 4 parametry:
        prvni_int - typu celé číslo (int)
        multiplikator - typu celé číslo
        seznam_celych_cisel - typu seznam celých čísel
        druhy_int - typu celé číslo a výchozí hodnota 0
    bude mít 1 atribut:
        vypoctena_hodnota - typu reálné číslo (float)
    hodnota vypoctena_hodnota je definována jako (prvni_int * multiplikator * sum(seznam_celych_cisel)) - druhy_int.
    porovnávání objektů musí být založeno pouze na hodnotách pole vypoctena_hodnota
    vytvořený objekt by měl být volatelný. Při zavolání musí vrátit hodnotu pole vypoctena_hodnota.
    Formát v jakém se objekt má vypsat na obrazovku pomocí funkce print je uveden níže v příkladech

Hodit se vám bude odkaz do dokumentace na modul dataclasses
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Tester:
    vypoctena_hodnota: float

    def __init__(self, prvni_int: int, multiplikator: int, seznam_celych_cisel: List[int], druhy_int=0):
        self.vypoctena_hodnota = (prvni_int * multiplikator * sum(seznam_celych_cisel)) - druhy_int

    def __call__(self, *args, **kwargs):
        return self.vypoctena_hodnota


t = Tester(2, 2, [2, 1], 9)
print(t)
print(t())

t = Tester(3, 5, [2, 2], 1)
print(t)
print(t())

t1 = Tester(3, 2, [2, 2], 1)
t2 = Tester(4, 1, [2, 4], 1)
print(t1())
print(t2())

print(t1 == t2)