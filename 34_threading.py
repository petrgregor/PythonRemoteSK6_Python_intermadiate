import threading


def iterovany_vypis(iterator):
    # Funkce vypíše prvky seznamu
    for prvek in iterator:
        print(prvek)


if __name__ == "__main__":
    # Vytvoří vlákna
    vlakno_1 = threading.Thread(target=iterovany_vypis, args=(range(5),))  # Výpis po sobě jdoucích přirozených čísel
    vlakno_2 = threading.Thread(target=iterovany_vypis, args=("Python",))  # Výpis znaků řetězce

    # Spustí vlákna
    vlakno_1.start()
    vlakno_2.start()

    # Čekání na dokončení obou vláken před spuštěním dalšího kódu.
    vlakno_1.join()
    vlakno_2.join()

    print("Hotovo!")
