# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

user_number1 = int(input('Please type your first integer number: '))
user_number2 = int(input('Please type your second integer number: '))

number_sum = user_number1 + user_number2

if number_sum > 100:
    print("Ok, your result is:", number_sum)
else:
    print("The end")
