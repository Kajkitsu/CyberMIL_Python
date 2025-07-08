# Ćwiczenie praktyczne 6 (FizzBuzz):
# Opracuj program FizzBuzz. Jest to program, który wyświetli liczby od 1 do 100.
# Dla liczb podzielnych przez 3 program powinien wyświetlić "Fizz", dla liczb podzielnych przez 5 "Buzz", a dla liczb podzielnych zarówno przez 3, jak i 5 "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
