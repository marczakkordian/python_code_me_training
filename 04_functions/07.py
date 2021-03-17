# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
def can_be_card_number(user_input) :
    if not len(user_input) in [13, 15, 16] :
        return False

    if not user_input.isdigit() :
        return False


def is_visa(card_number) :
    if card_number[0] == '4' and len(card_number) in [13, 16] :
        return True
    else :
        return False


def is_mastercard(card_number) :
    if (51 <= int(card_number[0 :2]) <= 55 or 2221 <= int(card_number[0 :4]) <= 2720) and len(card_number) == 16 :
        return True
    else :
        return False


def is_american_express(card_number) :
    if card_number[0 :2] in ['34', '37'] and len(card_number) == 15 :
        return True
    else :
        return False


# main code
user_input = input("Credit card number: ").replace(' ', '')

if can_be_card_number(user_input) :
    if is_visa(user_input) :
        print('Visa card')
    elif is_mastercard(user_input) :
        print('MasterCard')
    elif is_american_express(user_input) :
        print('American Express')
    else :
        print('Other card')
else:
    print('This input is not a card number')
