# funkce vezme text a vrátí ho malými písmeny
from dataclasses import dataclass


def to_lower(s):
    return s.lower()

print(to_lower("HA HA"))

lambda_function = lambda s: s.lower()
print(lambda_function("HA HA HA"))
print(lambda_function("HA HA HA HA"))


# funkce vezme číslo a vrátí její druhou mocninu
def square(x):
    return x ** 2

print(square(5))

lambda_square = lambda x: x ** 2
print(lambda_square(4))

# funkce vezme dva argumenty a vrátí True, pokud se rovnají
def equals(x, y):
    return x == y

lambda_equals = lambda x, y: x == y
print(lambda_equals(5, 5.0))

# map funkce: map(funkce, seznam argumentů)
# příklad: chceme všechny hodnoty seznamu dát na druhou
## pomocí for cyklu
my_list = [1, 2, 3, 4, 5]
results = []
for n in my_list:
    results.append(square(n))
print(f"results:    {results}")

## pomocí funkce map a definované funkce square
def square(x):
    return x ** 2
print(f"pomocí map: {list(map(square, my_list))}")
## to stejné pomocí labda výrazu
print(f"lambda:     {list(map(lambda x: x ** 2, my_list))}")

# funkce filter
## příklad: chceme vybrat pouze liché hodnoty
print("Funkce filter:")
my_list = [1, 2, 3, 4, 5]
results = []
for n in my_list:
    if n % 2 == 1:  # liché číslo (nepárné)
        results.append(n)
print(f"results:    {results}")

# to stejné pomofí filter
print(f"liché?:     {list(map(lambda x: x % 2 == 1, my_list))}")
print(f"lambda:     {list(filter(lambda x: x % 2, my_list))}")

# funkce reduce
from functools import reduce
# příklad: chceme sečíst všechny hodnoty v seznamu
print("Funkce reduce:")
my_list = [1, 2, 3, 4, 5]
result = 0
for n in my_list:
    result += n
print(f"Součet je:  {result}")

# pomocí funkce reduce
print(f"reduce:     {reduce(lambda x, y: x + y, my_list)}")

# sorted, max, min
pars = [(1, 10), (3, 9), (2, 8)]
print(f"sorted:     {sorted(pars)}")
print(f"sorted:     {sorted(pars, key=lambda x: x[1])}")
print(f"min:        {min(pars)}")
print(f"min:        {min(pars, key=lambda x: x[1])}")
print(f"max:        {max(pars)}")
print(f"max:        {max(pars, key=lambda x: x[1])}")

print(f"max:        {max(pars, key=lambda x: x[0] + x[1])}")

# definujte třídu Person, která bude mít atributy first_name a last_name
@dataclass
class Person:
    first_name: str
    last_name: str

# vytvořte několik instancí třídy Person
# vložte je do seznamu
persons = [Person("Martin", "Novák"),
           Person("Adéla", "Svobodová"),
           Person("Radim", "Brzobohatý")]

print(persons)

# úkol: uspořádat abecedně dle příjmení (last_name)
print(f"sorted by last_name:  {sorted(persons, key=lambda x: x.last_name)}")

# úkol: uspořádat abecedně dle jména (first_name)
print(f"sorted by first_name: {sorted(persons, key=lambda x: x.first_name)}")

# do třídy Person přidejte atribut salary (příjem)
@dataclass
class Person:
    first_name: str
    last_name: str
    salary: int

    def __repr__(self):
        return f"({self.first_name}, {self.last_name}, {self.salary})"

# vytvořte seznam
persons = [Person("Martin", "Novák", 25000),
           Person("Adéla", "Svobodová", 35000),
           Person("Radim", "Brzobohatý", 32500)]

# uspořádejte podle příjmu sestupně
print(f"sorted by salary:     {sorted(persons, key=lambda x: x.salary, reverse=True)}")  # sestupně
