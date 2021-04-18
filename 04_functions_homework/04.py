# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def is_number_within_range(numb, r):
    if numb in range(r):
        print(f'Yes, the number {numb} is within your range {r}')
    else:
        print(f'No, the number {numb} is out of your range {r}')


if __name__ == '__main__':
    usr_number = int(input('Please type your number: '))
    usr_range = int(input('Please type your range: '))
    is_number_within_range(usr_number, usr_range)
