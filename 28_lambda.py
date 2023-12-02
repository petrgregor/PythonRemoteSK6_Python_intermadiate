# funkce vezme text a vrátí ho malými písmeny
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

