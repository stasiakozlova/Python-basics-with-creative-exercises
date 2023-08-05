poem = '''И пьянчужки в парке, 
Лорды и кухарки,
Джефферсоновский шофёр
И китайский зубодёр,
Дети, женщины, мужчины - 
Винтики одной машины.
Все живём мы на Земле,
Варимся в одном котле.
Хорошо, хорошо, Это очень хорошо.'''

poem = poem.lower()
tire = poem.find(' -')
poem = poem[2:tire]

poem = poem.replace('\nи', ',')
poem = poem.replace('\n', '')
poem = poem.replace(', ', ',')
poem = poem.replace(' и ', ',')
people = poem.split(',')

print(people)

for person in people:
    print(person)


