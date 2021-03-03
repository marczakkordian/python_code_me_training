# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
#
#  numbers = input('Enter your numbers: ')
#  numbers.split(',')
#  print(numbers)
#
# print('Does the first and last number the same:', numbers[0 == numbers[-1]])

counter = int(input('Ile liczb chesz podać?'))

list_of_num = []
for i in range(counter):
    num = float(input('Podaj liczbę: '))
    list_of_num.append(num)

if list_of_num[0] == list_of_num[-1]:
    print('Pierwsza i ostatnia liczba taka sama')
else:
    print('Nie są takie same')