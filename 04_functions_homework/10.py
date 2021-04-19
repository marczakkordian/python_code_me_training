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
secret_word = random.choice(words)
print(secret_word)
usr_guesses = ''
word = ''
fails = 0


def show_word_to_user(word, secret_word, usr_guesses, fails):
    turns = 0
    while turns < 10:
        for i, char in enumerate(secret_word):
            if char in usr_guesses:
                word = word[:i] + char
            else:
                word = word[:i] + ''.join(char.replace(char, '- '))
                fails += 1
        print(word)
        word = ''

        if fails == 0:
            print("You Win")
            print(f'The correct word is: {secret_word}')
            break

        usr_guess = input("Type your letter: ").strip()
        usr_guesses += usr_guess

        if usr_guess in secret_word:
            print("Well done!")
        else:
            turns += 1
            print("Sorry, try again!")
            print(f'You have {10 - turns} more guesses')

        if turns == 10:
            print("You Loose")


if __name__ == '__main__':
    show_word_to_user(word, secret_word, usr_guesses, fails)
