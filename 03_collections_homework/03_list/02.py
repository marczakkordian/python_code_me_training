# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

usr_input = int(input('Please type your numbers: '))
print(usr_input)
even_nums = []

for number in usr_input:
    if number % 2 == 0:
        even_nums.append(number)

print(even_nums)
