import threading
import time


def iterovany_vypis(iterator):
    time.sleep(5)
    # Funkce vypíše prvky seznamu
    for prvek in iterator:
        print(prvek)
    return "Done"


if __name__ == "__main__":
    # Vytvoří vlákna
    vlakno_1 = threading.Thread(target=iterovany_vypis, args=(range(5),))  # Výpis po sobě jdoucích přirozených čísel
    vlakno_2 = threading.Thread(target=iterovany_vypis, args=("Python",))  # Výpis znaků řetězce

    # Spustí vlákna
    vlakno_1.start()
    vlakno_2.start()

    # Čekání na dokončení obou vláken před spuštěním dalšího kódu.
    result1 = vlakno_1.join()
    print(f"result1 = {result1}")
    vlakno_2.join()

    print("Hotovo!")
