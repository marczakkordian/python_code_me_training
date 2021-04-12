# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
import re

usr_input = input('Type your string: ')
cleaned_input = re.sub('[^A-Za-z]', '', usr_input.strip())

print('String slicing ==>', cleaned_input[1::2])

counter = 1
str_result = ''

for name in cleaned_input:
    if counter % 2 == 0:
        counter = counter + 1
        str_result = str_result + name
    else:
        counter = counter + 1

print(f'Loop result ==> {str_result}')
