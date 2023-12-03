import timeit

def linear_search(my_list, number):
    for item in my_list:
        if item == number:
            return True
    return False

def binary_search(my_list, number):
    low = 0
    high = len(my_list)
    mid = int((high+low)/2)
    while mid-low > 1:
        if my_list[mid] == number:
            return True
        elif my_list[mid] > number:
            high = mid
            mid = int((high+low)/2)
        else:
            low = mid
            mid = int((high + low) / 2)
    return False


# 1 2 6 9 10 15 16 19 25 26 105
# hledám 19
# a=0  b=11  mid_idx=5   mid_value=15


if __name__ == "__main__":
    nastaveni = '''
from __main__ import kod_linearni_vyhledavani, kod_binarni_vyhledavani
import random
def linear_search(my_list, number):
    for item in my_list:
        if item == number:
            return True
    return False
    
def binary_search(my_list, number):
    low = 0
    high = len(my_list)
    mid = int((high+low)/2)
    while mid-low > 1:
        if my_list[mid] == number:
            return True
        elif my_list[mid] > number:
            high =  mid
            mid = int((high+low)/2)
        else:
            low = mid
            mid = int((high + low) / 2)
    return False
'''

    kod_linearni_vyhledavani = '''
seznam = sorted([random.randint(0, 1000000) for _ in range(1000)])
hledane_cislo = random.randint(0, 1000000)
vysledek = linear_search(seznam, hledane_cislo)
'''

    kod_binarni_vyhledavani = '''
seznam = sorted([random.randint(0, 1000000) for _ in range(1000)])
hledane_cislo = random.randint(0, 1000000)
vysledek = binary_search(seznam, hledane_cislo)
'''

    print(timeit.timeit(stmt=kod_linearni_vyhledavani,
                        setup=nastaveni,
                        number=10))
    print(timeit.timeit(stmt=kod_binarni_vyhledavani,
                        setup=nastaveni,
                        number=10))