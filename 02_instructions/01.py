# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

user_number = int(input('Please type your integer number: '))


if user_number % 3 == 0:
    print("Ok, your number is dived by 3")
else:
    print("Sorry, your number is not dived by 3")
