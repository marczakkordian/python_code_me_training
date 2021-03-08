# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

# initializing user variable
user_str = input('Please enter your string of characters or type quit to leave the program:  ')

# the loop allowing the user enter string or quit
while user_str != 'quit':
    if len(user_str) > 5 and user_str.find('a') != -1:
        print('Your changed string: ', user_str.replace('a', 'i'))
        user_str = input('Ok - try again or quit:  ')
        # reset variable's value
    else:
        user_str = input('Sorry, try again or quit: ')
        # reset variable's value
