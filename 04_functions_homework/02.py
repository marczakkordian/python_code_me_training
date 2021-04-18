# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c)

def find_min_value(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3:
        return num2
    else:
        return num3


if __name__ == '__main__':
    print(find_min_value(2, 3, 1))
