# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

multi_table = []

for i in range(1, 11):
    multi_table.append([])
    for j in range(1, 11):
        multi_table[i-1].append([i*j])

print(multi_table)