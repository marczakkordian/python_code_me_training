import os

filename = 'example.txt'


def create_or_overwrite_file(filename) :
    with open(filename, 'w+') as fopen :
        usr_range = int(input('Type the number of lines: '))
        for i in range(usr_range) :
            fopen.write("This is line %d\r\n" % (i + 1))
    return os.stat(filename).st_size


print('Size of file in bytes: ', create_or_overwrite_file(filename))
