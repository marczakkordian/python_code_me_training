# Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji. Dane wejściowe pobierz z pliku csv (
# plik csv możesz traktować jako plik txt ze znanym znakiem podziału), który będzie przechowywał dane potrzebne do
# generowania. Przykład z generatora konferencji: http://generatorkonferencji.pl (niektóre potrafią wyjść zabawne).
# Wygenerujcie kilka. Czy widzicie wzorzec? Przykład generatora cytatów: http://wisdomofchopra.com/ (Można
# wykorzystać istniejące dane wejściowe json, lub przepisać na własny format danych).
import csv
import random

quote = ''

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    word_list = list(reader)

for element in word_list:
    random_ele = random.choice(element)
    quote = quote + ''.join(random_ele) + ' '

print(quote.title())
