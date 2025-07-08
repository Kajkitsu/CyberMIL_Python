# Ćwiczenie praktyczne 2:
# Rozbuduj poprzednio utworzony program o:
# Komunikat informujący o tym, w którym roku się urodziłeś

import datetime

imie = input("Podaj swoje imie: ")
wiek = int(input("Podaj swoj wiek: "))
aktualny_rok = datetime.date.today().year
rok_urodzenia = aktualny_rok - wiek
print(f"Cześć jestem {imie}, mam {wiek} lat.")
print(f"Urodziłeś się w {rok_urodzenia} roku.")
