from contextlib import contextmanager


@contextmanager
def spravce_souboru(nazev_souboru, mod):
    soubor = open(nazev_souboru, mod)
    print(f"Soubor '{nazev_souboru}' byl otevřen v modu '{mod}'")
    yield soubor
    soubor.close()
    print(f"Soubor '{nazev_souboru}' byl uzavřen")


if __name__ == "__main__":
    with spravce_souboru("test.txt", 'w') as soubor_zapis:
        soubor_zapis.write("Test")
