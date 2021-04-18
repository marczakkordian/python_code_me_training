# Utwórz słownik dla 10 krajów Europy zawierający listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystkie listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły co najmniej w 3 krajach.

names_dict = {'Albania': ['Amelia', 'Alja', 'Melisa', 'Amelija', 'Klea', 'Sara', 'Kejsi', 'Noemi', 'Alesia', 'Leandra'],
              'Andorra': ['Laia', 'Carlota', 'Emma', 'Lara', 'Martina', 'Aina', 'Maria', 'Blanca', 'Laura',
                          'Valentina'],
              'Austria': ['Anna', 'Hannah', 'Sophia', 'Emma', 'Marie', 'Lena', 'Sarah', 'Sophie', 'Laura', 'Mia'],
              'Belgium': ['Emma', 'Louise', 'Olivia', 'Elise', 'Alice', 'Juliette', 'Mila', 'Lucie', 'Marie',
                          'Camille'],
              'Bosnia and Herzegovina': ['Amina', 'Merjem', 'Sara', 'Asja', 'Lamija', 'Ema', 'Emina', 'Hana', 'Lejla',
                                         'Esma'],
              'Bulgaria': ['Viktoria', 'Maria', 'Nikol', 'Aleksandra', 'Gabriela', 'Daria', 'Raya', 'Yoana', 'Sofia',
                           'Simona'],
              'Croatia': ['Zuzanna', 'Lucija', 'Sara', 'Ana', 'Ema', 'Petra', 'Lana', 'Nika', 'Marta', 'Elena'],
              'Cyprus': ['Zuzanna', 'Eleni', 'Androula', 'Georgia', 'Panagiota', 'Anna', 'Christina', 'Katerina',
                         'Ioanna', 'Kyriaki'],
              'Czech Republic': ['Zuzanna', 'Tereza', 'Anna', 'Adéla', 'Natálie', 'Sofie', 'Kristýna', 'Karolína',
                                 'Viktorie', 'Barbora'],
              'Poland': ['Zuzanna', 'Julia', 'Lena', 'Maja', 'Hanna', 'Zofia', 'Amelia', 'Alicja', 'Aleksandra',
                         'Natalia']}
names_list = []
counting_table = []
result = []

# Conversion dict to nested table with 100 elements
for key, value in names_dict.items():
    for i in range(len(names_dict.values())):
        temp = [key, value[i]]
        names_list.append(temp)
        i += i
print(f' Names + country list: {names_list}')
print(f'Size of table: {len(names_list)}')

# Adding only names to counting table
for i in range(len(names_list)):
    for j in range(1, 2):
        counting_table.append(names_list[i][j])

# Count occurrence
for element in counting_table:
    counting_table.count(element)
    if counting_table.count(element) >= 3:
        temp = element, counting_table.count(element)
        result.append(temp)

set_res = set(result)
print(f'Names list with at least three time occurrence: {set_res}')
