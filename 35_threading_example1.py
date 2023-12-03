import timeit
import requests


def prochazej(url, vystupni_soubor):
    try:
        vysledek = requests.get(url).text
        with open(vystupni_soubor, "a") as soubor_zapis:
            soubor_zapis.write(vysledek)
    except requests.exceptions.RequestException:
        print("Problém s URL adresou!")


def prochazej_jednovlaknove(url_adresy):
    for url in url_adresy:
        prochazej(url, "jednovlaknove.txt")


def prochazej_vicevlaknove(url_adresy):
    import threading

    vlakna = []
    for url in url_adresy:
        vlakno = threading.Thread(target=prochazej, args=(url, "vicevlaknove.txt"))
        vlakno.start()
        vlakna.append(vlakno)

    for vlakno in vlakna:
        vlakno.join()


if __name__ == "__main__":
    jednovlaknove = "prochazej_jednovlaknove(urls)"
    vicevlaknove = "prochazej_vicevlaknove(urls)"

    nastaveni = '''
from __main__ import prochazej_jednovlaknove, prochazej_vicevlaknove

urls = [
    "https://jsonplaceholder.typicode.com/comments/1",
    "https://jsonplaceholder.typicode.com/comments/2",
    "https://jsonplaceholder.typicode.com/comments/3"
]
'''

    print("Jednovláknově:", timeit.timeit(stmt=jednovlaknove, setup=nastaveni, number=100))
    print("Vícevláknově:", timeit.timeit(stmt=vicevlaknove, setup=nastaveni, number=100))
