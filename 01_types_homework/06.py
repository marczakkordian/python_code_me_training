# Przekopiuj zawartość import this do zmiennej.
# >>> import this
# Policz liczbę wystąpień słowa better.
# Usuń z tekstu symbol gwiazdki
# Zamień jedno wystąpienie explain na understand
# Usuń spacje i połącz wszystkie słowa myślnikiem
# Podziel tekst na osobne zdania za pomocą kropki

string = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren\'t special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you\'re Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it\'s a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let\'s do more of those!"
print(string)
print(type(string))
print(len(string))

counter = string.count("better")
print(counter)
