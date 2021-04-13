# Napisz grę - kamień (k) / papier (p) / nożyce (n).
import random

print('Hello in the Rock Paper Scissors game!')
usr_number = int(input('Please type how many rounds you want play: '))
print('You can leave the game any time typing "end"')
usr_win, comp_win, draws = 0, 0, 0

for num in range(usr_number):
    usr_input = input('Please type your shape (r - rock, p - paper, s - scissors): ').lower()
    ran_shape = random.choice(['r', 'p', 's'])
    if usr_input == ran_shape:
        print('Draw!')
        draws = draws + 1
    elif usr_input == 'r' and ran_shape == 'p':
        print("Computer's win!")
        comp_win = comp_win + 1
    elif usr_input == 'r' and ran_shape == 's':
        print('Your win!')
        usr_win = usr_win + 1
    elif usr_input == 'p' and ran_shape == 'r':
        print('Your win!')
        usr_win = usr_win + 1
    elif usr_input == 'p' and ran_shape == 's':
        print("Computer's win!")
        comp_win = comp_win + 1
    elif usr_input == 's' and ran_shape == 'r':
        print("Computer's win!")
        comp_win = comp_win + 1
    elif usr_input == 's' and ran_shape == 'p':
        print('Your win!')
        usr_win = usr_win + 1
    elif usr_input == 'end':
        print('Game closed by the User')
        break

print(f'Final results. Your wins: {usr_win} || Computer wins {comp_win} || Draws: {draws}')
print('The game is closed')
