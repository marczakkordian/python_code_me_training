# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = input('Please enter your first word: ')
s2 = input('Please enter your second word: ')

middle = len(s1) // 2

s3 = s1[0:middle] + s2 + s1[middle:]

print(s3)
