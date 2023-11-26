import json
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    surname: str
    points: int


students = []
with open("students.json", encoding='utf-8') as students_file:
    students_dict = json.load(students_file)
    print(students_dict)
    #students.append(students_dict['students'][0]['name'])


# export do json souboru
students2 = [
        {
            'jméno': "Adam",
            'příjmení': "Novák",
            'počet_bodů': 20
        },
        {
            'jméno': "Anna",
            'příjmení': "Rychlá",
            'počet_bodů': 17
        }
    ]

with open("studenti.json", 'w', encoding='utf-8') as students_file:
    json.dump(students2, students_file, indent=2, ensure_ascii=False)  # zápis s odsazením 2 mezery
    # If ensure_ascii is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped.
    # If ensure_ascii is false, these characters will be output as-is.