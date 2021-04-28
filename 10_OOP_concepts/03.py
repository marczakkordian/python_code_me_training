# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.

class Pen:
    def __init__(self):
        print("So crazy, here's a pen")


class Pineapple:
    def scream(self):
        print("So crazy, here's a pineapple")


class PenPineapple(Pen, Pineapple):
    def __init__(self):
        super().__init__()
        super().scream()


if __name__ == '__main__':
    strange_thing = PenPineapple()
