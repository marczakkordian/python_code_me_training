# # my mood example function
# def ask_about_mood():
#     question = 'How are you?'
#     print(question)
#
#
# def show(user_response):
#     print('^^^', user_response, '^^^')
#
# def multiple_sentence(counter):
#     sentence = 'I love Python!'
#     return sentence * counter
#
# # main part of the code
# print('*********')
# ask_about_mood()
#
# response = input('--> answer here: ')
# show(response)
#
# print(multiple_sentence(5))
# print('-----END----')
def get_books():
    counter = int(input('How many books do you want to add to the collection?: '))

    books_collection = []
    for book in range(counter):
        tittle = input('Book title: ')
        rate = int(input(f'{tittle} - rate [0-10]: '))
        books_collection.append([tittle, rate])

    return books_collection


def show_rate(books_list):
    nr = int(input('Which rate you want to see?: '))
    index = nr - 1

    if nr > len(books_list) or nr < 0:
        print('No such book in collection')
    else:
        print(f'Book ==> {books_list[index][0]} is rated ==> {books_list[index][1]} / 10')

#-------- main part ---------
print('Welcome to library! -------')
books = get_books()
print('Added!')
print('---------------------------')
show_rate(books)