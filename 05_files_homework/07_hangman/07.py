# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc.
# Poproś użytkownika o podanie kategorii przed rozpoczęciem gry.
# Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.
import random

usr_guesses = ''
word = ''
fails = 0


def chose_word_category(user_category):
    if user_category == 'food':
        with open('food.txt', 'r') as f:
            content = f.read()
            random_word = random.choice(content.split('\n')).lower()
            return random_word
    elif user_category == 'science':
        with open('science.txt', 'r') as f:
            content = f.read()
            random_word = random.choice(content.split('\n')).lower()
            return random_word
    elif user_category == 'animals':
        with open('animals.txt', 'r') as f:
            content = f.read()
            random_word = random.choice(content.split('\n')).lower()
            return random_word


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
    secret_word = chose_word_category(str(input('Please choose your category (food, science, animals): ').lower()))
    print(secret_word)
    show_word_to_user(word, secret_word, usr_guesses, fails)
