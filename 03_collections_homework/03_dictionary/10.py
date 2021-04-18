# Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany
# jest jej kwadrat (n : n * n).
# Załóżmy, że użytkownik podał N = 8
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
usr_dict = {}
usr_numb = int(input('Please enter your number: '))

for i in range(usr_numb):
    i = i + 1
    keys = i
    values = i * i
    usr_dict[keys] = values

print(usr_dict)

