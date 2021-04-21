# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach:marka (str) model (str) rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć,
# czy program również zmienia swoje zachowanie.

my_dict = {'marka': 'Opel', 'model': 'Astra', 'rocznik': '1958'}


def is_older_than_25_years():
    if 2021 - int(my_dict.get('rocznik')) >= 25:
        print(f'Gratulacje! Twój samochód {my_dict["model"]} może być zarejestrowany jako zabytek')
    else:
        print(f'Twój samochód {my_dict["model"]} jest jeszcze zbyt młody.')


# main code
print(my_dict)
is_older_than_25_years()
