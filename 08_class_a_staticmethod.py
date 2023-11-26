# TODO: Úkol: ošetřit chyby při nesprávném vstupu:
#  + záporný věk
#  + záporná hodnota stipendia
#  + nevyplěné stipendium
#  - špatně zadané jméno (počáteční velké písmeno)


class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} má {self.vek} let"


class Student(Osoba):
    def __init__(self, jmeno, vek, stipendium):
        if self.jmeno_ve_spravnem_formatu(jmeno):
            Osoba.__init__(self, jmeno, vek)
            self.stipendium = stipendium
        # TODO: není else, pokud není jméno ve správném formátu, nevyplní se nic.
        else:
            raise AttributeError

    def vrat_vydelek(self):
        return self.stipendium

    @classmethod
    def vytvor_z_retezce(cls, retezec):
        # jmeno, vek, stipendium = retezec.split()
        splited = retezec.split(',')
        #print(splited)
        """if len(splited) == 0:
            raise AttributeError
        jmeno = splited[0]
        if len(splited) > 1:
            vek = splited[1]
            if len(splited) > 2:
                stipendium = splited[2]
            else:
                stipendium = 0
        else:
            vek = None
            stipendium = 0
        """

        jmeno = splited[0]
        # TODO: pokud jméno začíná malým písmenek, tak ho zvětšíme.
        try:
            vek = int(splited[1])
            if vek < 0:
                vek = None
        except:
            vek = None
        try:
            stipendium = float(splited[2])
            if stipendium < 0:
                stipendium = 0
        except:
            stipendium = 0
        #vek, stipendium = int(vek), float(stipendium)
        #if cls.jmeno_ve_spravnem_formatu(jmeno):
        return cls(jmeno, vek, stipendium)

    @staticmethod
    def jmeno_ve_spravnem_formatu(jmeno):
        if jmeno[0].isupper() and len(jmeno) >= 2:
            return True
        return False


students = []
"""
try:
    students.append(Student("Markéta", 32, 0))
    students.append(Student("Jan", 25, 2000))
    students.append(Student("martin", 24, 2300))  # zde se to zastaví
    students.append(Student("Radek", 24, 2300))   # Radek se již nevytvoří
except:
    pass
"""

students_str = ["Markéta,-32,0", "Jan,25,-2000", "martin,21,2500", "Radek,26,0", "Petr,25,", "Petra,,2500"]
for student_str in students_str:
    try:
        students.append(Student.vytvor_z_retezce(student_str))
    except AttributeError:
        pass

for student in students:
    print(f"{student} má stipendium ve výši {student.stipendium}")

"""
student_1 = Student("markéta", 32, 0)
student_2 = Student.vytvor_z_retezce("Jana 21 600")
print(student_1)
print(student_2)
print(Student.jmeno_ve_spravnem_formatu("alice"))
"""