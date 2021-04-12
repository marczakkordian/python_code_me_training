# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.
import re
specialChars = '@'
usr_input = str(input('Please enter your names(with separator ";"): '))
cleaned_input = usr_input.strip().replace(specialChars, '').title().split(';')

for name in cleaned_input:
    print(f'Hello {name}!')