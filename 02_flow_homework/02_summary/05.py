# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komputer odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

ran_num = random.randrange(1, 100)
usr_num = int(input('Type your number (1-100): '))
diff_init = 0
diff_num = 0
counter = 1

diff_init = abs(usr_num - ran_num)
if usr_num == ran_num:
    print('Congrats! You won the game :)')
elif diff_init <= 10:
    print('Hot!')
else:
    print('Cold!')

while counter <= 6 and usr_num != ran_num:
    usr_num = int(input('Type your next number: '))
    diff_num = abs(usr_num-ran_num)
    diff_last = diff_init
    if usr_num == ran_num:
        print('Congrats! You won the game :)')
    elif diff_num == diff_init or diff_num == diff_last:
        counter = counter + 1
        print('No change! Type different number.')
    elif diff_num <= diff_last:
        counter = counter + 1
        diff_last = diff_num
        print('Hotter')
    elif diff_num >= diff_last:
        print('Colder!')
        counter = counter + 1
        diff_last = diff_num

print('Sorry, you reached maximum of attempts (6). Computer wins!')

