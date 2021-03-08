# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

# defining secret number
secret_num = 12
# defining user number variable
user_num = int(input('Enter your number (1-20): '))

# loop with guessing number
while secret_num != user_num:
    user_num = int(input('Sorry, try again: '))

# condition for winning case
print('Congrats! You won the game')