import timeit


def odpocitavej(od, do):
    while od >= do:
        od -= 1


def odpocitavej_jednovlaknove():
    odpocitavej(400000, 0)


def odpocitavej_vicevlaknove():
    import threading

    vlakno_1 = threading.Thread(target=odpocitavej, args=(400000, 200000))
    vlakno_2 = threading.Thread(target=odpocitavej, args=(200000, 0))
    # vlakno_3 = threading.Thread(target=odpocitavej, args=(200000, 100000))
    # vlakno_4 = threading.Thread(target=odpocitavej, args=(100000, 0))

    vlakno_1.start()
    vlakno_2.start()
    # vlakno_3.start()
    # vlakno_4.start()

    vlakno_1.join()
    vlakno_2.join()
    # vlakno_3.join()
    # vlakno_4.join()


def odpocitavej_paralelne():
    import multiprocessing

    p1 = multiprocessing.Process(target=odpocitavej, args=(400000, 200000))
    p2 = multiprocessing.Process(target=odpocitavej, args=(200000, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    jednovlaknove = "odpocitavej_jednovlaknove()"
    vicevlaknove = "odpocitavej_vicevlaknove()"
    paralelne = "odpocitavej_paralelne()"
    nastaveni = "from __main__ import odpocitavej_jednovlaknove, odpocitavej_vicevlaknove, odpocitavej_paralelne"

    print("Jednovláknově:", timeit.timeit(stmt=jednovlaknove,
                                          setup=nastaveni,
                                          number=10))
    print("Vícevláknově:", timeit.timeit(stmt=vicevlaknove,
                                         setup=nastaveni,
                                         number=10))
    print("Paralelně:", timeit.timeit(stmt=paralelne,
                                      setup=nastaveni,
                                      number=10))

