# Zadanie 7 (Obliczanie BMI):
# Napisz program, który pobierze od użytkownika wagę (w kilogramach) i wzrost (w metrach), a następnie obliczy i wyświetli indeks masy ciała (BMI) zgodnie z poniższym wzorem: BMI = masa / (wzrost^2)

waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi = waga / (wzrost ** 2)
print(f"Twoje BMI wynosi: {bmi:.2f}")
