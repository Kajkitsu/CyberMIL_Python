# Zadanie 12 (Palindrom):
# Napisz program, który sprawdzi, czy podane przez użytkownika słowo jest palindromem
# (czyli czy czyta się tak samo od lewej do prawej i od prawej do lewej, np. "kajak" czy "anna").

slowo = input("Podaj słowo: ")
slowo_odwrocone = ""

# Pętla do odwrócenia słowa
for litera in slowo:
    slowo_odwrocone = litera + slowo_odwrocone

# Sprawdzenie, czy słowo jest takie samo jak jego odwrócona wersja
if slowo.lower() == slowo_odwrocone.lower():
    print(f"Słowo '{slowo}' jest palindromem.")
else:
    print(f"Słowo '{slowo}' nie jest palindromem.")
