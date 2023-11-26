import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice má kočku", "Programování v Pythonu je skvělé"),
    'c': [False, True, False]
}

with open('data.pickle', 'wb') as soubor:
    # pracuji se souborem
    pickle.dump(data, soubor)
    # stále pracuji se souborem

# zde již soubor není dostupný (automaticky se uzavře)
