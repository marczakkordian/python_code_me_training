# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
#
# >>>  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

res_list = [i for n, i in enumerate(example_list) if i not in example_list[n + 1:]]
print(res_list)
tup_list = tuple(res_list)
print(f'Min value: {min(tup_list)}, Max value: {max(tup_list)} ')