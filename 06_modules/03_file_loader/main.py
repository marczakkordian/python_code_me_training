import file_loader as fl

if __name__ == '__main__':
    print(fl.read_file('test.txt'))

    text_to_save = 'Lalalalal'
    print(fl.save_file('save.txt', text_to_save))
