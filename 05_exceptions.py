# Chceme dělit číslo 3 všemi kladnými hodnotami v seznamu 'number'

# TODO: Úkol: napsat vlastní výjimku pro dělení záporným číslem (chceme dle zadání dělit pouze kladnými)
class NegativeNumber(Exception):
    def __init__(self):
        message = "Nastala výjimka záporné dělení"
        super().__init__(message)

numbers = [-1, 2, 0, 3, 5, -5, 0, "five"]

errors = []

def divide(a, number):
    if number < 0:
        raise NegativeNumber
    return a / number

def get_result(a, number):
    return f"{a} / {number} = {divide(a, number)}"

def my_function(a, numbers):
    try:
        f = open("results.txt")
        for number in numbers:
            print(get_result(a, number))
            f.write(get_result(a, number))
        f.close()
    except FileNotFoundError:
        for number in numbers:
            try:
                print(get_result(a, number))
                c = a + b
                assert a == number

            except (ZeroDivisionError, TypeError):
                #print("Nastala chyba ZeroDivisionError nebo TypeError")
                errors.append(f"Nastala chyba ZeroDivisionError nebo TypeError pro hodnotu '{number}'")
            #except TypeError:
            #    pass
            except AssertionError:
                #print("Nastala chyba AssertionError")
                errors.append(f"Nastala chyba AssertionError pro hodnotu a={a}, number={number}")
            except NegativeNumber:
                errors.append(f"Nastala výjimka NegativeNumber pro hodnotu {number}")
            except:
                #print("Nastala jiná chyba")
                errors.append(f"Nastala jiná chyba")


my_function(3, numbers)

print("Výpis chyb:")
for error in errors:
    print(error)