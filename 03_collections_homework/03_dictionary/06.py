#  Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
#
# >>> days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days = [{'Jan': 31, 'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}]

# first solution -- list comprehension
# res_list = [i for n, i in enumerate(days) if i not in days[n + 1:]]
# print(res_list)

# second solution -- naive method
res_list = []
for i in range(len(days)):
    if days[i] not in days[i + 1:]:
        res_list.append(days[i])

print(days)
