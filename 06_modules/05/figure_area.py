import os


def safe_read_file(filename):
    try:
        with open(filename, mode='r', encoding='UTF-8') as file:
            file_size = os.stat(filename)
            if file_size.st_size == 0:
                return "File is empty"
            reader = file.read()
            return reader
    except FileNotFoundError:
        return "File not found."


def save_write_to_file(filename):
    text_to_file = "Lalalala"
    try:
        with open(filename, mode='w', encoding='UTF-8') as file:
            file_size = os.stat(filename)
            if file_size.st_size != 0:
                return "File is not empty"
            reader = file.write(text_to_file)
            return reader

    except FileNotFoundError:
        return "File not found."


if __name__ == '__main__':
    print(safe_read_file('text.txt'))
    print(save_write_to_file('text.txt'))
