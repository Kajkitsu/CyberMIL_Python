# Zadanie 10 (Liczenie wystąpień litery):
# Napisz program, który pobierze od użytkownika string oraz literę i policzy, ile razy ta litera występuje w podanym stringu.

tekst = input("Podaj tekst: ")
litera = input("Podaj literę do zliczenia: ")
ilosc = tekst.count(litera)
print(f"Litera '{litera}' występuje w tekście {ilosc} razy.")
