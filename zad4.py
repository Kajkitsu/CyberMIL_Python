# Ćwiczenie praktyczne 4:
# Rozbuduj poprzednio utworzony program o:
# Pętlę, która poinformuje Cię, w którym roku będziesz miał ile lat, przez najbliższe 10 lat.
# Przykład: „W roku 2024 będziesz miał 50 lat…”, „W roku 2025 będziesz miał 51 lat…”

import datetime

wiek = int(input("Podaj swoj wiek: "))
aktualny_rok = datetime.date.today().year

for i in range(10):
    print(f"W roku {aktualny_rok + i} będziesz miał {wiek + i} lat.")
