# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

list2D = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]
counter = len(list2D)
for index in range(counter):
    print(index + 1, ' - '.join(list2D[index]))



