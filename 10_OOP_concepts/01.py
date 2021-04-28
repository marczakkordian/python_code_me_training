# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.

class Mammals:
    def __init__(self, name):
        print("I'm mammal and my name is", name)


class Cat(Mammals):
    def __init__(self, cat_name):
        print("I'm cat and my name is", cat_name)
        super().__init__(cat_name)


class Dog(Mammals):
    def __init__(self, dog_name):
        print("I'm dog and my name is", dog_name)
        super().__init__(dog_name)


class Human(Mammals):
    def __init__(self, person_name):
        print("I'm human and my name is", person_name)
        super().__init__(person_name)


if __name__ == '__main__':
    person = Human('John')
    dog = Dog('Dyzio')
    cat = Cat('Meow')
