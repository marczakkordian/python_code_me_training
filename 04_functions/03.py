# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
# HM wszystkie zadania do 6

def sum_list(arr):
    sum_items = 0
    for item in arr:
        sum_items += item

    return sum_items

# main part

result = sum_list([1, 2, 3, 1])
print(result)