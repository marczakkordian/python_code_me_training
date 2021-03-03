# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

# word = 'kajak'
# print("Is palindrom: ", word == word[::-1])

sentence = input('Gimme me a sentence? ')
sentence = sentence.replace(" ", "")
sentence = sentence.lower()

print(sentence)
print("Is palindrom: ", sentence == sentence[::-1])
