"""
Úkol 1

Napište třídu správce kontextu, která vypíše dobu trvání spuštěného kódu.

"Nápověda" Ve funkci __enter__ uložte aktuální čas a ve funkci __exit__
odečtěte aktuální čas od uloženého času (zmíněného dříve).
"""
import datetime
import time
from dataclasses import dataclass, field
from io import TextIOWrapper


@dataclass
class MyContextManager:
    file_name: str
    mode: str
    file: TextIOWrapper = field(init=False)
    start_time: datetime.datetime = field(init=False)

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        self.file = open(self.file_name, self.mode)
        print(f"Soubor '{self.file_name}' byl úspěšně otevřen v modu '{self.mode}'.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f"Soubor '{self.file_name}' byl úspěšně uzavřen.")
        print(f"Trvání: {datetime.datetime.now() - self.start_time}")


if __name__ == "__main__":
    with MyContextManager('ukol1.txt', 'w') as file:
        file.write("Pokus")
        time.sleep(5)