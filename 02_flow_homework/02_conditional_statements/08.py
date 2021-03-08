# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

# getting data from user
first_numb = float(input('Enter first number: '))
second_numb = float(input('Enter second number: '))
third_numb = float(input('Enter third number: '))

# creating list with numbers
numbers = [first_numb, second_numb, third_numb]
# sorting numbers
numbers_sorted = sorted(numbers)
# result printing
print('The biggest number is:', max(numbers_sorted), '\nYour sorted numbers:', numbers_sorted)


