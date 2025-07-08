# Zadanie 11 (Suma liczb parzystych):
# Napisz program, który pobierze od użytkownika liczbę całkowitą i obliczy sumę wszystkich liczb parzystych od 0 do podanej liczby.

liczba = int(input("Podaj liczbę: "))
suma = 0
for i in range(0, liczba + 1, 2):
    suma += i
print(f"Suma liczb parzystych od 0 do {liczba} wynosi: {suma}")
