# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

usr_number = int(input('Enter a number between 1 and 100: '))
magic_number = 58

if usr_number == magic_number:
    print('Congrats!!! You won ;)')
elif usr_number != magic_number:
    print('Miss!!! Try again')
else:
    print('Something went wrong. Sorry')
