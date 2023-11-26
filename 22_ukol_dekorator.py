# napište dekorátor, který pro danou funkci spočítá a vypíše, jak dlouho
# trval výpočet

# TODO dekorátor pro výpis doby trvání dané funkce
def execution_time():
    pass

# funkce pro Fibonacci
def fib(n):
    if not isinstance(n, int):
        raise ValueError("Lze zadat pouze celé číslo")
    if n < 1:
        raise ValueError(f"Nelze hledat {n}-tý člen posloupnosti")
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

# funkce pro výpočet faktoriálu (rekurzivně)
# fact(5) = 5*4*3*2*1
# fact(5) = 5*fact(4)
# fact(4) = 4*fact(3)
# fact(1) = 1
# fact(0) = 1
def fact(n):
    if not isinstance(n, int):
        raise ValueError("Lze zadat pouze celé číslo")
    if n < 0:
        raise ValueError("Fakrotiál nelze počítat pro záporné hodnoty.")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))
print(fib(15))

