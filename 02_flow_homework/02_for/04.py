# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

# user input
n = int(input('Please type integer number (0-8): '))
s = 1
t = []

if n > 8:
    n = int(input('Please type correct integer number (0-8): '))
elif 0 <= n < 2:
    for n in range(0, 1):
        s = 1
    print(n, "! = ", s)
else:
    for n in range(1, n + 1):
        t.append(n)
        s = s * n
    t_convert = str(t)
    print(n, "! =\n", t_convert.replace(',', ' *'), ' = ', s)
