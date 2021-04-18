# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
# Dopisz odpowiednie komunikaty.

my_dict = {'marka': 'Opel', 'model': 'Astra', 'rocznik': '1958', 'czy-oryginalny': 'false'}


def is_vintage(boolean):
    if 2021 - int(my_dict.get('rocznik')) >= 25:
        return True
    else:
        return False


def is_original(boolean):
    if my_dict.get('czy-oryginalny') == 'true':
        return True
    else:
        return False


# main code
print(my_dict)
if is_vintage() is True and is_original() is True:
    print(f'Gratulacje! Twój samochód {my_dict["model"]} może być zarejestrowany jako zabytek')
else:
    print(f'Twój samochód {my_dict["model"]} jest jeszcze zbyt młody lub ma nieoryginalne części.')
