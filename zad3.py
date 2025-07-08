# Ćwiczenie praktyczne 3:
# Rozbuduj poprzednio utworzony program o:
# Komunikat informujący o tym czy jesteś zwolniona/y z podatku dochodowego

import datetime

imie = input("Podaj swoje imie: ")
wiek = int(input("Podaj swoj wiek: "))
aktualny_rok = datetime.date.today().year
rok_urodzenia = aktualny_rok - wiek

print(f"Cześć jestem {imie}, mam {wiek} lat.")
print(f"Urodziłeś się w {rok_urodzenia} roku.")

if wiek < 26:
    print("Jesteś zwolniony/a z podatku dochodowego.")
else:
    print("Nie jesteś zwolniony/a z podatku dochodowego.")
