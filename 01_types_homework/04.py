# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

book_tittle = input('Please enter your book tittle: ')
lastname_of_author = input('Please enter a lastname of the author: ')
pages_number = input("Please enter your book's pages number: ")

check_isLetters_inTittle = str.istitle(book_tittle)
print('Your tittle has only letters', check_isLetters_inTittle)

check_isLetter_inLastname = str.istitle(lastname_of_author)
print('Your lastname of the author has only letters', check_isLetter_inLastname)

check_isNumber_inPages = str.isnumeric(pages_number)
print('Your number of pages has only numbers', check_isNumber_inPages)

seq = (book_tittle, lastname_of_author, pages_number)
s = " "
book = s.join(seq)
print('All data into one string:', book)

char_lenght = len(book)
print("Total amount of chars:", char_lenght)
