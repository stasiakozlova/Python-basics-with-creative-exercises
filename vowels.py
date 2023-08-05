while True:
    vowels = {'а', 'е', 'о', 'у', 'ы', 'и', 'э', 'я', 'ё', 'ю'}
    word = input('Введите слово: ')
    found = vowels.intersection(set(word))
    print ('В слове ', word, ' такие гласные: ', found)
    question = input('Хотите продолжить? ')
    if question == 'нет':
        break
