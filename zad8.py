# Zadanie 8 (Liczby pierwsze):
# Napisz program, który pobierze od użytkownika liczbę i sprawdzi, czy jest ona liczbą pierwszą (czyli podzielną tylko przez 1 i samą siebie).

liczba = int(input("Podaj liczbę: "))
jest_pierwsza = True
if liczba < 2:
    jest_pierwsza = False
else:
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            jest_pierwsza = False
            break

if jest_pierwsza:
    print(f"Liczba {liczba} jest liczbą pierwszą.")
else:
    print(f"Liczba {liczba} nie jest liczbą pierwszą.")
