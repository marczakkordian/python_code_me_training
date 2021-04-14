mail_list = ['first@mail.com', 'second@mail.com', 'third@mail.com', 'fourth@mail.com']
searched = 'first@mail.com'


def is_searched_mail_on_list(list, mail):
    for element in mail_list:
        if element == searched:
            return True
    return False


print(is_searched_mail_on_list(mail_list, searched))