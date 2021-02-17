#1
result = str.isnumeric("1232a323")

print(result)

#2
result2 = str.center("Python", 15, "*")

print(result2)

#3
result3 = "Remove_this_string".strip("ing")
print(result3)

#4


#5

#1.1
quote = 'Honesty is the first chapter in the book of wisdom.'

print(len(quote))
print(quote[-7:-1])
middle = len(quote)//2
print(middle)
print(quote[0:middle])
print(quote[-1])
print(quote[middle::3])
print(quote[0::2])
print(quote[::-2])
print(quote[::-1])
print(quote.replace("wisdom","friendship"))

