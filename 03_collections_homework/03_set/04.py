# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]

input_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
result = []

div_num = int(len(input_list) / 3)
first = 0
last = div_num


for element in range(first, int(last)):
    if last <= len(input_list):
        result = input_list[first: last]
        print(result[::-1])
        first += div_num
        last += div_num

