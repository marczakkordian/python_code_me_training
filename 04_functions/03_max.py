# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_of_2(arg_1, arg_2):
    return arg_1 if arg_1 > arg_2 else arg_2
    # if arg_1 > arg_2:
    #     return arg_1
    # else:
    #     return arg_2


def maximum_of(a, b, c):
    # temp = maximum_of_2(a, b)
    # max_of_abc = maximum_of_2(c, maximum_of_2(a, b))
    return maximum_of_2(c, maximum_of_2(a, b))
    # if c > max_of_ab:
    #     return c
    # else:
    #     return max_of_ab


print(maximum_of(10, 7, 8))