# dekorátory
from datetime import datetime


def vypni_v_noci(funkce):
    # Dekorátor, který volá dekorovanou funkci pouze během dne.
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            funkce()

    return wrapper


@vypni_v_noci
def pozdrav():
    print("Ahoj Světe")


def pozdrav_bez_dekoratoru():
    if 7 <= datetime.now().hour < 22:
        print("Ahoj Světe")

pozdrav_bez_dekoratoru()
pozdrav()
#vypni_v_noci(pozdrav())

def pust_v_rozpeti(od=7, do=22, function_name=""):
    # Dekorátor, který volá dekorovanou funkci pouze v zadaném časovém rozpětí
    def dekorator(dekorovana_funkce):
        def wrapper():
            if od <= datetime.now().hour < do:
                print(f"Výpis z funkce {function_name} {datetime.now()}: ", end="")
                dekorovana_funkce()

        return wrapper

    return dekorator


@pust_v_rozpeti(9, 14, "pozdrav2")
def pozdrav2():
    print("Ahoj Světe")


@pust_v_rozpeti(9, 20, "pozdrav3")
def pozdrav3():
    print("Ahoj Světe")

pozdrav2()
pozdrav3()
