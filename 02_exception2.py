def divide(a, b):
    print("   # divide")
    return a / b

def my_function(a, b):
    print("  # my_function")
    try:
        print(f"{a} / {b} = {divide(a,b)}")
    except ZeroDivisionError:
        print("my_function: Nastala vyjímka dělení nulou!")

# my_function(6, 2)

def my_iteration(number, elements):
    print(" # my_iteration")
    for element in elements:
        print(" # element = {element}")
        try:
            my_function(number, element)
        except ZeroDivisionError:
            print("my_iteration: Nastala vyjímka dělení nulou!")

print("# Main")
try:
    my_iteration(3, [1,0,2])
except ZeroDivisionError:
    print("Main: Nastala vyjímka dělení nulou!")