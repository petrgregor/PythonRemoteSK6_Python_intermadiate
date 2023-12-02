from math import sqrt


# TODO: optimalizovat tuto funkci
def je_prvocislo(cislo):
    for i in range(2, int(sqrt(cislo)) + 1):
        if cislo % i == 0:
            return False
    return True


def vrat_n_prvocisel(n):
    prvocisla = []
    i = 2
    while len(prvocisla) != n:
        if je_prvocislo(i):
            prvocisla.append(i)
        i += 1
    return prvocisla

"""
seznam_prvocisel = vrat_n_prvocisel(1000000)
for prvocislo in seznam_prvocisel:
    print(prvocislo)
"""

class PrvocislaIterator:
    # Iterátor pro iteraci nad n prvočísly
    def __init__(self, n):
        self.n = n
        self.vygenerovana_cisla = 0
        self.cislo = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cislo += 1
        if self.vygenerovana_cisla >= self.n:
            raise StopIteration
        elif je_prvocislo(self.cislo):
            self.vygenerovana_cisla += 1
            return self.cislo
        return self.__next__()


iterator = PrvocislaIterator(1000000)
for prvek in iterator:
    print(prvek)

"""
n       vygenerovana_cisla      cislo
1000000                  0          1
                         1          2
                         2          3
                         2          4
                         3          5
"""