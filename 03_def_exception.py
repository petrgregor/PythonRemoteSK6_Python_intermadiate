# metoda 1
class NulovyDelitel(Exception):
    # Definice vlastní třídy, která dědí z generické třídy Exception
    pass

try:
    cislo = 3
    prvky = [1, 0, 2]
    for prvek in prvky:
        if prvek == 0:
            raise NulovyDelitel("Dělitel nemůže být nula")
        vysledek = cislo / prvek
        print(f"Výsledek je: {vysledek}")
except NulovyDelitel:
    pass

# metoda 2
class NulovyDelitel2(Exception):
    def __init__(self):
        zprava = "Dělitel nemůže být nula"
        super().__init__(zprava)


try:
    cislo = 3
    prvky = [1, 0, 2]
    for prvek in prvky:
        if prvek == 0:
            raise NulovyDelitel2()
        vysledek = cislo / prvek
        print(f"Výsledek je: {vysledek}")
except NulovyDelitel2:
    print("Dělitel nemůže být nula")
