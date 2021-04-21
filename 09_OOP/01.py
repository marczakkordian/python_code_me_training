class Dog:
    def __init__(self, name, colour, bred):
        self.name = name
        self.colour = colour
        self.bred = bred

    def bark(self):
        return 'hau'

    def wag_tail(self):
        return 'wag a tail'


reksio = Dog('reksio', 'black', 'mutt')

print(Dog.bark(reksio))     # first way
print(reksio.wag_tail())    # second way
