from bs4 import BeautifulSoup

with open('sokirko_overall.txt', 'r') as f:
    soup = BeautifulSoup(f, features="html.parser")

print(soup.prettify())

words = soup.find_all('w')
total_words = len(words)
print('Всего слов: ', total_words)

obs = soup.find_all('ob')
total_obs = len(obs)
print('Всего слов: ', total_obs)

total_words_in_obs = 0
for ob in obs:
    words_in_ob = ob.find_all('w')
    total_words_in_obs += len(words_in_ob)
print('Всего слов в оборотах: ', total_words_in_obs)
print('Всего слов вне оборотов: ', total_words - total_words_in_obs)

razbory = soup.find_all('ana')
for razbor in razbory:
    if ('мр, ' in razbor['gram']) and (razbor['pos'] == 'С'):
        print(razbor['lemma'])

print(len(words))
print(words[0])
print(words[1])
print(words[10])

print()
print(len(razbory))
print(razbory[0])
print(razbory[1])
print(razbory[10])

print('\nА теперь - атрибут!')
print(razbory[0]['gram'])
print(razbory[1]['gram'])
print(razbory[10]['gram'])

