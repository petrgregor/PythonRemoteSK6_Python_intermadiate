import timeit

nastaveni = "from math import sqrt"

kod = '''
def funkce():
    return [sqrt(x) for x in range(100)]
'''

print(timeit.timeit(stmt=kod, setup=nastaveni))
