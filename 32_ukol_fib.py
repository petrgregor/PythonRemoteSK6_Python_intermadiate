import random
import string
from datetime import datetime, timedelta
from math import sqrt

# vytvořte iterátor nebo generátor, který bude iterovat/generovat
#  Fibonaciho posloupnost
#  0 1 1 2 3 5 8 13 ...
print("Fibonacci")
def fibonacci_gen(n):
    n1, n2 = 0, 1
    yield n1
    yield n2
    i = 2
    while i <= n:
        n1, n2 = n2, n1+n2
        yield n2
        i += 1
        """
        sum_n = n1+n2
        n1 = n2
        n2 = sum_n
        yield sum_n
        i += 1
        """

fibonacci_generator = fibonacci_gen(15)

for number in fibonacci_generator:
    print(number, end=", ")
print()

# lambda výraz pro vytvořní seznamu druhých mocnin: 1, 4, 9, 16, 25, ...
print("lambda výraz pro vytvořní seznamu druhých mocnin")
square_numbers = list(map(lambda x: x**2, range(1,11)))
print(square_numbers)

# lambda výraz pro vyfiltrování slov delších než 5 znaků
words = ['Ahoj', 'Nazdar', "Čau", "Sbohem", "Nashledanou"]
print("lambda výraz pro vyfiltrování slov delších než 5 znaků")
def word_length_filter(words, l):
    result = []
    for word in words:
        if len(word) > l:
            result.append(word)
    return result

print(word_length_filter(words, 5))
print(list(filter(lambda w: len(w) > 5, words)))

# lambda výraz pro vyfiltrování slov délky 3 až 7 znaků
print("lambda výraz pro vyfiltrování slov délky 3 až 7 znaků")
print(list(filter(lambda w: 3 <= len(w) <= 7, words)))

# lambda výraz pro vyfiltrování slov začínající velkým písmenem
print("lambda výraz pro vyfiltrování slov začínající velkým písmenem")
words = ['Ahoj', 'Nazdar', "Čau", "sbohem", "Nashledanou"]
print(list(filter(lambda w: w[0].isupper(), words)))

# lambda výraz pro vyfiltrování palindromů
print("lambda výraz pro vyfiltrování palindromů")
words = ['ABBA', 'radar', 'a', 'anna', 'hannah', 'hana', 'ahoj']
print(list(filter(lambda w: w == w[::-1], words)))

# generátor druhých mocnin
print("generátor druhých mocnin")
def pow_two_gen(n=0):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1

pow_two_generator = pow_two_gen(10)

for i in pow_two_generator:
    print(i, end=" ")
print()

# generátor náhodných slov zadané délky
def word_gen(n=0, l=0):
    i = 0
    while i < n:
        yield ''.join(random.choice('ABCDEFabcdef01234ěščřž') for _ in range(l))
        i += 1

word_generator = word_gen(10, 7)

for word in word_generator:
    print(word)

# stream = nekonečný generátor
# mocniny dvojky: 1, 2, 4, 8, 16, 32, ...
def bin_pow_gen():
    number = 1
    while True:
        yield number
        number *= 2

bin_pow_generator = bin_pow_gen()

#for number in bin_pow_generator:
#    print(number)

print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))
print(next(bin_pow_generator))


# TODO: generátor všech permutací zadané množiny (bez knihovny itertools)
# permutace -> pořadí
# například pro množinu ['a', 'b', 'c']
# ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')

# TODO: generátor všech kombinací zadané množiny (bez knihovny itertools)
# například pro množinu ['a', 'b', 'c']
# dvouprvkové kombinace: ('a', 'b'), ('a', 'c'), ('b', 'c')

# TODO: generátor všech podmnožin zadané množiny (bez knihovny itertools)
# například pro množinu ['a', 'b', 'c']
# {}, {'a'}, {'b'}, {'c'}, {'a', 'b'}, {'a', 'c'}, {'b', 'c'}, {'a', 'b', 'c'}

# generátor všech dělitelů zadaného čísla
# např. 12 -> 1, 2, 3, 4, 6, 12
def div_number(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i

div_number_generator = div_number(357)

for number in div_number_generator:
    print(number)

# generátor pro rozklad na prvočinitele
# 12 -> 2*2*3=12
# 13 -> 13
print("generátor pro rozklad na prvočinitele")
def is_prime(cislo):
    for i in range(2, int(sqrt(cislo)) + 1):
        if cislo % i == 0:
            return False
    return True


def prime_numbers_gen(n):
    # Generátor pro iteraci nad n prvočísly
    cislo = 2
    while cislo <= n:
        if is_prime(cislo):
            yield cislo
        cislo += 1

def prime_factorization(n):
    prime_numbers_generator = prime_numbers_gen(n)
    prime = next(prime_numbers_generator)
    while n != 1:
        if n % prime == 0:
            yield prime
            n = n / prime
        else:
            prime = next(prime_numbers_generator)

prime_factorization_generator = prime_factorization(13)

for number in prime_factorization_generator:
    print(number)

# generátor pro pracovní dny - od dnešního data (včetně) vygeneruje n dní
print("generátor pro pracovní dny")
date = datetime(2023, 12, 8)
print(f"Den {date} je {date.weekday()} ")

def working_days_gen(n):
    i = 0
    date = datetime.now()  # today
    while i < n:
        if date.weekday() < 5:  # working day
            yield date
            i += 1
        date = date + timedelta(days=1)

working_days_generator = working_days_gen(12)

for day in working_days_generator:
    print(f"Den {day} je {day.weekday()} ")

# generátor pro pracovní dny - od zadaného data do zadaného data
print("generátor pro pracovní dny - od zadaného data do zadaného data")
def working_days_gen2(from_day, to_day):
    actual_date = from_day
    while actual_date <= to_day:
        if actual_date.weekday() < 5:  # working day
            if actual_date.month == 1 and actual_date.day == 1:  # vynecháme 1. leden (svátek)
                pass
            else:
                yield actual_date
        actual_date = actual_date + timedelta(days=1)


from_date = datetime(2024, 1, 1)
to_date = datetime(2024, 1, 31)
working_days_generator = working_days_gen2(from_date, to_date)

for day in working_days_generator:
    print(f"Den {day.strftime('%d. %m. %Y')} je {day.weekday()} ")


# pipeline -> spojování generátorů
print("pipeline -> spojování generátorů")
def square(numbers):
    for number in numbers:
        yield number**2

for number in square(fibonacci_gen(10)):
    print(number)

print(f"Součet = {sum(square(fibonacci_gen(10)))}")

print("Rozdíl mezi 'list comprehension' a generátorem")
print("List comprehension")
even_numbers = [i*2 for i in range(1,1000001)]
"""
for number in even_numbers:
    print(number, end=" ")
"""

print("\nGenerátor")
def even_numbers_gen(n):
    for i in range(1, n+1):
        yield i*2

"""
for number in even_numbers_gen(10):
    print(number, end=" ")
print()
"""

from pympler import asizeof
print(f"Velikost seznamu:    {asizeof.asizeof(even_numbers)}")
print(f"Velikost generátoru: {asizeof.asizeof(even_numbers_gen(1000000))}")
