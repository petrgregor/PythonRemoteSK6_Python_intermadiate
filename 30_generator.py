from math import sqrt


def je_prvocislo(cislo):
    for i in range(2, int(sqrt(cislo)) + 1):
        if cislo % i == 0:
            return False
    return True


def generator_prvocisel(n):
    # Generátor pro iteraci nad n prvočísly
    cislo = 2
    vygenerovana_cisla = 0
    while vygenerovana_cisla != n:
        if je_prvocislo(cislo):
            yield cislo, vygenerovana_cisla
            vygenerovana_cisla += 1
        cislo += 1


generator = generator_prvocisel(1000000)
print("První blok")
for prvek in generator:
    if prvek[0] > 100:
        break
    print(prvek)

print("Druhý blok")
for prvek in generator:
    if prvek[0] > 200:
        break
    print(prvek)
