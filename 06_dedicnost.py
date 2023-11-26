class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} má {self.vek} let"


class Zamestnanec(Osoba):
    def __init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin):
        Osoba.__init__(self, jmeno, vek)
        self.sazba = sazba
        self.pocet_odpracovanych_hodin = pocet_odpracovanych_hodin

    def vrat_vydelek(self):
        return self.sazba * self.pocet_odpracovanych_hodin

    def __str__(self):
        return f"Zaměstnanec {self.jmeno} má {self.vek} let"


class Student(Osoba):
    def __init__(self, jmeno, vek, stipendium):
        Osoba.__init__(self, jmeno, vek)
        self.stipendium = stipendium

    def vrat_vydelek(self):
        return self.stipendium

    def __str__(self):
        return f"Student {self.jmeno} má {self.vek} let"


class PracujiciStudent(Zamestnanec, Student):
    def __init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin, stipendium):
        Zamestnanec.__init__(self, jmeno, vek, sazba, pocet_odpracovanych_hodin)
        Student.__init__(self, jmeno, vek, stipendium)

    def vrat_vydelek(self):
        return self.sazba * self.pocet_odpracovanych_hodin + self.stipendium

    def __str__(self):
        return f"Pracující zaměstnanec {self.jmeno} má {self.vek} let"

os1 = Osoba("Jan", 54)
os2 = Zamestnanec("Romana", 36, 20, 160)
os3 = Student("Alena", 22, 1000)
print(os1)
try:
    print(f"{os1} a vydělává {os1.vrat_vydelek()}")
except:
    pass
print(f"{os2} a vydělává {os2.vrat_vydelek()}")
print(f"{os3} a vydělává {os3.vrat_vydelek()}")

os4 = PracujiciStudent("Monika", 24, 9.5, 70, 550)
print(f"{os4} a vydělává {os4.vrat_vydelek()}")