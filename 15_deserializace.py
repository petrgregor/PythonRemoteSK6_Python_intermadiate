import pickle

with open('data.pickle', 'rb') as soubor:
    data = pickle.load(soubor)

print(data)
print(data['a'][3])