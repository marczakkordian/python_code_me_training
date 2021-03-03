# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Please type your password: ")

lenght_correct = len(password) >= 8
includes_letters_and_digits = password.isalnum() and not password.isdigit() and password.isalpha()
at_least_one_capital_letter = not password.islower()

if not lenght_correct:
    print("Your password is to short, please try again")

if not includes_letters_and_digits:
    print("Your password should contain letters and digits, please try again")

if not at_least_one_capital_letter:
    print("Your password should contain at least one capital letter, please try again")
