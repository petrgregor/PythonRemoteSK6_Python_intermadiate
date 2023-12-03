import re

pattern = r"[A-Z]la"
print(re.search(pattern, "ala Ola Ela"))

print(re.match(pattern, "ala Ola Ela"))

print(re.fullmatch(r"[A-Z]la", "Ela"))

print(re.findall(r".la", "Ola ala Ela"))

iterator_pres_shody = re.finditer(r".la", "Ola ala Ela")
for shoda in iterator_pres_shody:
    print(shoda)

print(re.split(r",|\.", "jablko,hruška,hrozny,mrkev.zelí,zelenina.ovoce,dvůr"))

print(re.sub(r"[a-z]{5}", "psa", "Alice má slona a kocku"))

print(re.subn(r"[a-z]{5}", "psa", "Alice má slona a kocku"))


text = "Tomas W. (33), naposledy viden v Brne"
vzor = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+)\)"
shoda = re.search(vzor, text)
print(shoda)
print(shoda.groups())
print(shoda.group(0))
print(shoda.group(1))
print(shoda.group(2))

text = "Tomáš (33) a Eva (24) se dohodli, ze spolu zitra pujdou na nakup"
vzor = r"([A-Z]{1}[a-záčďéěíľňóřšťúůýž]+) \((\d+)\)"
print(re.findall(vzor, text))

pattern = r"[A-Z]{1}[\w\u0100-\u017F]+"
print(re.findall(pattern, text))

"""
Najděte všechna čísla ze zadaného textu pomocí regulárního výrazu.

Tj. pro řetězec "test43543lfdsfdsfl534543fdgl432fr" to bude:

    43543
    534543
    432

"Nápověda" Použijte speciální symbol \d, který označuje libovolnou číslici, a znak +, 
který znamená "jeden nebo více znaků".
"""

text = "test43543lfdsfdsfl534543fdgl432fr"
pattern = r"\d+"
numbers = re.findall(pattern, text)
print(f"numbers: {numbers}")

# pomocí compile
pattern = re.compile(r"\d+")
numbers = pattern.findall(text)
print(f"numbers: {numbers}")

# součet - verze pomocí cyklu
result = 0
for number in numbers:
    result += int(number)
print(f"Součet = {result}")
# součet - verze pomocí lambda výrazu
print(f"Součet = {sum(map(lambda x: int(x), numbers))}")

# TODO: napsat regulární výraz, který kontroluje validní email
# TODO: napsat regulární výraz, který kontroluje validní rodné číslo

