seznam = [1, 2, 3, 4]

for i in range(10):
    try:
        print(f"i={i}: {seznam[i]}")
    except IndexError:
        print(f"Index {i} je mimo rozsah.")

print("###########")
try:
    for i in range(1000000):
        print(f"i={i}: {seznam[i]}")
except IndexError:
    print(f"Index {i} je mimo rozsah.")