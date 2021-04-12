# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

usr_input = input('Type your string: ')

l, u, d, s = 0, 0, 0, 0

for i in usr_input:
    if 'a' <= i <= 'z':
        l = l + 1
    elif 'A' <= i <= 'Z':
        u = u + 1
    elif '0' <= i <= '9':
        d = d + 1
    else:
        s = s + 1

print(f'Low characters: {l}\nUpper characters: {u}\nNumbers: {d}\nSpecial characters: {s}')
