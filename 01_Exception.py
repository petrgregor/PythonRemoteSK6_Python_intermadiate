number = 3
elements = [1, 0, 2]

print("'IF' version")
for element in elements:
    if element != 0:
        result = number / element
        print(f"Result = {result}")

print()
print("'TRY' version")
for element in elements:
    try:
        result = number / element
        print(f"Result = {result}")
        result = number / (element-1)
    except ZeroDivisionError:
        print("Dělení nulou.")
        # continue