# Porównaj zachowanie discard() vs remove() dla typu set.
input_set = {10, 20, 30, 40, 50, 60, 70}

# remove -- error is raised when element doesn't exist

# input_set.remove(10)
# print(input_set)
# input_set.remove(100)
# print(input_set)

# discard -- no error in case attempt to remove not existing element

# input_set.discard(10)
# print(input_set)
input_set.discard(100)
print(input_set)