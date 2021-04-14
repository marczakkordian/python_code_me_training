# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
odd_nums = []


usr_nums = input('Please type 10 numbers: ').split()
print(len(usr_nums))

if len(usr_nums) == 10:
    for number in usr_nums:
        if int(number) % 2 != 0:
            odd_nums.append(number)
        else:
            continue
else:
    print('Please type 10 numbers!')

print('Odd numbers within yours numbers:', odd_nums)
