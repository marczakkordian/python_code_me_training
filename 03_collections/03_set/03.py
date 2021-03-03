# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8)
tuple_2 = (9, 10, 11, 12, 13, 14)

my_list = list(tuple_1[::2])
print(my_list)
my_list2 = list(tuple_2[1::2])
print(my_list2)

set_all = set(my_list + my_list2)
print(set_all)