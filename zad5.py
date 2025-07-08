# Ćwiczenie praktyczne 5:
# Opracuj nowy program służący do konwersji temperatury ze stopni Celsjusza na stopnie Fahrenheita.
# Program, pobierze od użytkownika temperaturę w stopniach Celsjusza i przeliczy ją na stopnie Fahrenheita zgodnie z poniższym wzorem: F = (C * 9/5) + 32

celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C to {fahrenheit}°F")
