# napište dekorátor, který pro danou funkci spočítá a vypíše, jak dlouho
# trval výpočet
from datetime import datetime


# TODO dekorátor pro výpis doby trvání dané funkce
def duration_time(function):
    start_time = datetime.now()
    def decorator(args):
        result = function(args)
        if args == 1:
            end_time = datetime.now()
            total_time = end_time - start_time
            print(f"ČAS: {total_time}")
        return result

    return decorator


def starter(func):
    def decorator(args):
        return func(args)

    return decorator


# TODO funkce pro Fibonacci
@duration_time
@starter
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)


print("Fibonacci")
print(fib(15))


# TODO funkce pro výpočet faktoriálu (rekurzivně)
# fact(5) = 5*4*3*2*1
# fact(5) = 5*fact(4)
# fact(4) = 4*fact(3)
# fact(1) = 1
# fact(0) = 1
@duration_time
@starter
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print("Factorial")
print(fact(250))