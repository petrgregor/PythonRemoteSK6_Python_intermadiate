class SpravceSouboru():
    def __init__(self, nazev_souboru, mod):
        self.nazev_souboru = nazev_souboru
        self.mod = mod
        self.soubor = None

    def __enter__(self):
        # Zpřístupnění a sdílení zdrojů
        self.soubor = open(self.nazev_souboru, self.mod)
        return self.soubor

    def __exit__(self, typ, hodnota, trasovani_chyby):
        # Čištění a uvolňování zdrojů
        self.soubor.close()


if __name__ == "__main__":
    with SpravceSouboru("test.txt", 'w') as soubor_zapis:
        soubor_zapis.write("Test")
