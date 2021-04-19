# Wyświetl 3 losowe cytaty z quotes.txt
import random


def read_from(file):
    with open(file) as fp:
        content = fp.read()
    return content


def random_line(lines):
    ran_lines = random.choices(lines.split('\n'), k=3)
    return ran_lines


filename = 'quotes.txt'
file_lines = read_from(filename)
print(random_line(file_lines))