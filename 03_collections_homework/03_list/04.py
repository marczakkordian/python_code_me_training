# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

even_list = []

usr_input = input('Type your elements (use space as a delimiter): ').split()
even_list = usr_input

if len(even_list) % 2 == 0:
    middle_ele = int(len(even_list) / 2)
    compared_ele = middle_ele - 1
    if even_list[middle_ele] == even_list[compared_ele]:
        print(f'Middle elements on your list {even_list[middle_ele]} and {even_list[compared_ele]} are the same')
    else:
        print(f'Middle elements on your list {even_list[middle_ele]} and {even_list[compared_ele]} are NOT the same')
else:
    print("Sorry, something went wrong!")

