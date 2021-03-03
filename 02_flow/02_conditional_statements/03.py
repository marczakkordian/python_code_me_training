# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.


first_rate = float(input("Please type first rate (0-10): "))
second_rate = float(input("Please type second rate (0-10): "))
third_rate = float(input("Please type third rate (0-10): "))
sum = first_rate + second_rate + third_rate
average = sum/3

if average >= 7:
    print("Very good rate", average)
elif average < 7 and sum >= 5:
    print("Average rate", average)
elif average < 5:
    print("It's not worth to watch")
else:
    print("Something went wrong", average)