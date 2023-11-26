# vytvořte třídu Book, která bude obsahovat atributy pro:
# název,
# autor,
# rok vydání
# vydavatelství
# počet stran
import csv
import json
import pickle
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    publisher: str
    pages: int

    def __repr__(self):
        return f"Kniha ['title': {self.title}, 'author': {self.author}]"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __dict__(self):
        return {"title": self.title,
                "author": self.author,
                "year": self.year,
                "publisher": self.publisher,
                "pages": self.pages}

# vytvořte několik instancí
book1 = Book("Egypťan Sinuhet", "Mika Waltari", 2013, "Český klub", 830)
book2 = Book("Hlava 22", "Joseph Heller", 2018, "Slovart (SK)", 408)
book3 = Book("Malý princ", "Antoine de Saint-Exupéry", 2014, "Albatros", 96)
book4 = Book("Tulák po hvězdách", "Jack London", 2001, "Labyrint", 333)

# knihy vložte do nějaké kolekce: "library"
library = [book1, book2, book3, book4]
print(f"Original library: {library}")

# tuto knihovnu uložte do souboru
with open('library.pickle', 'wb') as file:
    pickle.dump(library, file)

# znovu načtěte ze souboru "knihovnu"
# with open('library.pickle', 'rb') as file:
#     library2 = pickle.load(file)
#     print(library2)


# exportovat knihovnu do csv souboru (včetně hlavičky)
with open("library.csv", "w", encoding='utf-8', newline='') as library_file:
    writer = csv.writer(library_file)
    writer.writerow(['title', 'author', 'year', 'publisher', 'pages'])
    for book in library:
        writer.writerow([book.title, book.author, book.year, book.publisher, book.pages])


# importovat knihovnu z csv souboru
library_csv = []
with open("library.csv", "r", encoding='utf-8') as library_file:
    reader = csv.reader(library_file)
    next(reader)
    for book in reader:
        library_csv.append(Book(book[0], book[1], int(book[2]), book[3], int(book[4])))

print(f"Import from csv:  {library_csv}")

# exportovat knihovnu do json souboru
with open("library.json", "w", encoding='utf-8') as library_file:
    library_list = []
    for book in library:
        library_list.append(book.__dict__())
    library_dict = {"books": library_list}
    json.dump(library_dict, library_file, indent=2, ensure_ascii=False)

# importovat knihovnu z json souboru
library3 = []
with open("library.json", "r", encoding='utf-8') as library_file:
    library_json = json.load(library_file)
    #print(library_json)
    for book in library_json["books"]:
        #print(book)
        library3.append(Book(book['title'],
                             book['author'],
                             book['year'],
                             book['publisher'],
                             book['pages']))

print(f"Import from JSON: {library3}")