# Stwórz grę wisielec “bez wisielca”.
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użytkownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wypadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.
import random

words = ['python', 'java', 'science', 'computer', 'testing', 'learning']
turns = 0
secret_word = random.choice(words)
print(secret_word)
usr_guesses = ''
n_char = ''

while turns < 10:
    fails = 0
    for i, char in enumerate(secret_word):
        if char in usr_guesses:
            n_char = n_char[:i] + char
        else:
            n_char = n_char[:i] + ''.join(char.replace(char, '- '))
            fails += 1
    print(n_char)
    n_char = ''

    if fails == 0:
        print("You Win")
        print(f'The correct word is: {secret_word}')
        break

    usr_guess = input("Type your letter: ").strip()
    usr_guesses += usr_guess

    if usr_guess in secret_word:
        print("Well done!")

    if usr_guess not in secret_word:
        turns += 1
        print("Sorry, try again!")
        print(f'You have {10 - turns} more guesses')

    if turns == 10:
        print("You Loose")
