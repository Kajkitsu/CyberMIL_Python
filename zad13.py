# Zadanie 13 (Zamiana systemów liczbowych):
# Napisz program, który pobierze od użytkownika liczbę w systemie dziesiętnym
# i przeliczy ją na system binarny, ósemkowy i szesnastkowy.

liczba_dec = int(input("Podaj liczbę dziesiętną: "))

# Konwersja na system binarny
temp_liczba = liczba_dec
binarnie = ""
if temp_liczba == 0:
    binarnie = "0"
while temp_liczba > 0:
    reszta = temp_liczba % 2
    binarnie = str(reszta) + binarnie
    temp_liczba = temp_liczba // 2
print(f"Binarnie: {binarnie}")

# Konwersja na system ósemkowy
temp_liczba = liczba_dec
osemkowo = ""
if temp_liczba == 0:
    osemkowo = "0"
while temp_liczba > 0:
    reszta = temp_liczba % 8
    osemkowo = str(reszta) + osemkowo
    temp_liczba = temp_liczba // 8
print(f"Ósemkowo: {osemkowo}")

# Konwersja na system szesnastkowy
temp_liczba = liczba_dec
szesnastkowo = ""
mapa_hex = "0123456789ABCDEF"
if temp_liczba == 0:
    szesnastkowo = "0"
while temp_liczba > 0:
    reszta = temp_liczba % 16
    szesnastkowo = mapa_hex[reszta] + szesnastkowo
    temp_liczba = temp_liczba // 16
print(f"Szesnastkowo: {szesnastkowo}")
