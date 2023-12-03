import threading
import time


class VlaknoSNavratovouHodnotou(threading.Thread):
    def __init__(self, funkce, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.funkce = funkce
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.vysledek = self.funkce(*self.args, **self.kwargs)

    def join(self, casovy_limit=None):
        super().join(casovy_limit)
        return self.vysledek


def vypis_treti_mocninu(cislo):
    # Funkce, která vrací třetí mocninu čísla zadaného jako parametr
    time.sleep(5)
    print(f"Třetí mocnina: {cislo * cislo * cislo}")


def vrat_druhou_mocninu(cislo):
    # Funkce, která vrací druhou mocninu čísla zadaného jako parametr
    time.sleep(5)
    return cislo * cislo


if __name__ == "__main__":
    # Vytvoření vláken
    t1 = VlaknoSNavratovouHodnotou(funkce=vrat_druhou_mocninu, args=(10,))
    t2 = threading.Thread(target=vypis_treti_mocninu, args=(10,))
    t3 = VlaknoSNavratovouHodnotou(funkce=vrat_druhou_mocninu, args=(20,))

    # Spuštění vláken
    t1.start()
    t2.start()
    t3.start()

    # Čekání na dokončení obou vláken před spuštěním dalšího kódu
    result1 = t1.join()
    result2 = t3.join()
    print(f"result = {result1 + result2}")
    t2.join()

    print("Hotovo!")
