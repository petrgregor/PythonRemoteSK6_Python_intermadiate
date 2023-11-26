
def fact(n):
    if not isinstance(n, int):
        raise ValueError("Lze zadat pouze celé číslo")
    if n < 0:
        raise ValueError("Fakrotiál nelze počítat pro záporné hodnoty.")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*fact(n-1)

print("Tato část kódu proběhne vždy.")

if __name__ == "__main__":
    print("Tato část kódu se spustí pouze v případě, kdy se jedná o 'hlavní' soubor.")
    print(fact(5))
