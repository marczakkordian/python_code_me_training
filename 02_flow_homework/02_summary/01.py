# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.
import re

# taking data from user and filtering
usr_input = str(input('Please enter your names(with separator ";"): '))
cleaned_input = re.sub('[^A-Za-z;]', '', usr_input.strip())
cleaned_input = cleaned_input.split(';')

# hello loop
for name in cleaned_input:
    print(f'Hello {name}!')
