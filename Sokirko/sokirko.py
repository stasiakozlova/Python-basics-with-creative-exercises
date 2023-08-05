lemmas = 0
punctuation_lemmas = 0
lemmas_outside_phrase = 0
ambiguous_words = 0
unambiguous_words = 0
different_pos = 0
total_ana = 0
total_ob = 0
outside_phrase = True

f = open('MM1standalone.txt', 'r')

for line in f:
    # отмечаем вход в оборот или выход из него
    if '<ob>' in line:
        outside_phrase = False
        total_ob += 1
    elif '</ob>' in line:
        outside_phrase = True

    if '<w>' in line:
        lemmas += 1
        if outside_phrase:
            lemmas_outside_phrase += 1
        lemmas_tmp = 0
        different_pos_tmp = set()
    elif '<pun>' in line:
        punctuation_lemmas += 1
    elif '<ana' in line:
        total_ana += 1
        lemmas_tmp += 1
        pos_first_part = line.split('pos="')[1]
        pos_second_part = pos_first_part.split('"')[0]
        different_pos_tmp.add(pos_second_part)
    elif '</w>' in line:
        if lemmas_tmp == 1:
            unambiguous_words += 1
        elif lemmas_tmp > 1:
            ambiguous_words += 1
        if len(different_pos_tmp) > 1:
            different_pos += 1
            
            



f.close()

print(f'Всего токенов: {lemmas}')
print(f'Всего токенов вместе со знаками препинания: {lemmas + punctuation_lemmas}')
print(f'Всего словарных словоформ, не считая внутри оборотов: {lemmas_outside_phrase}')
print(f'Однозначных разборов (слов): {unambiguous_words}')
print(f'Многозначных разборов (слов): {ambiguous_words}')
print(f'Процент многозначности: {ambiguous_words*100/lemmas}%')
print(f'Многозначных разборов, где многозначность выражается в отнесении слова к разным частям речи (слов): {different_pos}')
print(f'«Частеречная» многозначность по отношению к многозначным разборам в целом: {different_pos*100/ambiguous_words}%')
print(f'Всего вариантов анализа: {total_ana}')
print(f'Среднее число вариантов на 1 слово: {total_ana/lemmas}')
print(f'Всего оборотов: {total_ob}')
