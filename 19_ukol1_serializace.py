# Napište program, který vypíše průměr čísel z pole "prava_strana",
# průměr z pole "leva_strana" a průměr z obou polí.
import json
#from statistics import mean

def mean(numbers):
    # TODO: opravit
    return sum(numbers)/len(numbers)

data = {}
with open("cv_serializace_ukol1.json") as file:
    data = json.load(file)

print(data)
print(f"Průměr pravé strany: {round(sum(data['prava_strana']) / len(data['prava_strana']), 3)}")
print(f"Průměr levé strany:  {round(sum(data['leva_strana']) / len(data['leva_strana']), 3)}")
data_all = data['prava_strana'] + data['leva_strana']
print(f"Průměr obou stran:   {round(sum(data_all) / len(data_all), 3)}")

# pomocí modulu statistics
print(f"Průměr pravé strany: {round(mean(data['prava_strana']), 3)}")
print(f"Průměr levé strany:  {round(mean(data['leva_strana']), 3)}")
data_all = data['prava_strana'] + data['leva_strana']
print(f"Průměr obou stran:   {round(mean(data_all), 3)}")

print(f"Průměr s prázdným seznamem:     {round(mean([]), 3)}")
print(f"Průměr s nečíselnou hodnotou:   {round(mean([1, 2, 3, 'a']), 3)}")
