# TODO: máme firmu, kde si v informačním systému ukládáme informace o zaměstnancích (jméno, příjmení, plat)
#  + automaticky se novému zaměstnanci vygeneruje nové ID a přidá timestamp (čas, kdy byl přidán do databáze).
import datetime
import time

# TODO pomocí iterátoru
class IdIterator:

    def __init__(self, n):
        self.n = n
        self.last_id = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last_id += 1
        return self.last_id


#id_iterator = IdIterator(500)


class Person:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.id = None # next(id_iterator)  #None  # TODO: generate id
        self.timestamp = datetime.datetime.now()
        time.sleep(0.3)

    def __repr__(self):
        return f"{self.first_name}\t\t{self.last_name}\t\t{self.id}\t{self.timestamp}"


persons = [Person("Martin", "Novák", 35000),
           Person("Adéla", "Nová", 41000),
           Person("Roman", "Těžký", 35700)]

print("first name\tlast name\tid\t\ttimestamp")
print("-"*60)
#for person in persons:
    #print(f"{next(IdIterator)} {person}")




# TODO pomocí generátoru

