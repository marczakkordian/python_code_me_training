# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
# Zadbaj o sposób wyświetlania np.:
#
# szybko : 5
#
# zbudź : 1

my_str = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

my_str = my_str.lower()
my_str = my_str.replace(',', ' ')
my_str = my_str.split()

# print(my_str)

my_str_dict = {}
for word in my_str:
    if word in my_str_dict:
        my_str_dict[word] += 1
    else:
        my_str_dict[word] = 1
for key, value in my_str_dict.items():
    print(key, ':', value)
