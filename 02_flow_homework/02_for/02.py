# Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy po kolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
filename = 'recipe.txt'
recipe = []


def load_recipe_file():
    try:
        with open(filename, 'r', encoding='utf-8-sig') as fopen:
            lines = fopen.readlines()
        for line in lines:
            line = line.strip('\n').split()
            recipe.append(line)
    except FileNotFoundError as error:
        print(f"FIle {filename} doesn't exist", error)


def print_recipe():
    print('*' * 60 + '\n' + 'Spaghetti Pasta Carbonara\n' + '*' * 60)
    print('List of ingredients:\n' + '*' * 60)
    for element in recipe:
        element = str(element).strip('[' + ']' + "'").replace(',', '').replace("'", "")
        print(f'Add {element}')
    print('Method:\n' + '*' * 60)
    print(
        '1) Heat pasta water\n' + '2) Sauté pancetta/bacon and garlic\n' + '3) Beat eggs and half of the cheese\n' + '4) '
                                                                                                'Cook pasta\n' + '*' * 60)


if __name__ == '__main__':
    load_recipe_file()
    print_recipe()
