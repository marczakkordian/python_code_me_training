# Przekopiuj zawartość import this do zmiennej.
# >>> import this
# Policz liczbę wystąpień słowa better.
# Usuń z tekstu symbol gwiazdki
# Zamień jedno wystąpienie explain na understand
# Usuń spacje i połącz wszystkie słowa myślnikiem
# Podziel tekst na osobne zdania za pomocą kropki

s: str = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than " \
         "implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than " \
         "nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren\'t special enough to break " \
         "the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly " \
         "silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably " \
         "only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you\'re Dutch.\nNow " \
         "is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to " \
         "explain, it\'s a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces " \
         "are one honking great idea -- let\'s do more of those! "
print(s)
print(type(s))
print(len(s))

# 1 count appearance of 'better'
counter = s.count('better')
print('#1', 'better', counter)

# 2 remove '*' character
s_2 = s.replace('*', '')
print('#2', s_2, '*', counter)

# 3 change one occurrence of 'explain' to 'understand'
s_3 = s.replace('explain', 'understand', 1)
print('#3', s_3)

# 4 remove spaces and replace them '-' character
s_4 = s.replace(' ', '-')
print('#4', s_4)

# 5 split text using '.' separator
s_5 = s.split('.')
print('#5', s_5)
