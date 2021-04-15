# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
num_tuple = (1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 1)
repeated_num = []

for ele in num_tuple:
    if num_tuple.count(ele) > 1:
        repeated_num.append(ele)
    else:
        continue

print(f'Repeated elements: {repeated_num}')