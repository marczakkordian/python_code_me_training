# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
# drukowanymi lub zaczynając od dużej litery)
import re
import sys

usr_num = 1
item_table = []
res_table = []

while usr_num <= 5:
    usr_input = input(f'User {usr_num} | Type your 4 school items and use semicolon as a separator : ').casefold().strip().split(';')
    for item in usr_input:
        item_table.append(item)
    usr_num = usr_num + 1

for element in item_table:
    count = item_table.count(element)
    temp = element, count
    res_table.append(temp)

print(f'Most popular item with the number of occurrence is {max(res_table, key=lambda x: x[1])}')
