from pprint import pprint

results = {'Иванова': {'Макулатура': 3, 'Металлолом': 1, 'Морковь': 4},
           'Петров': {'Макулатура': 10, 'Металлолом': 12, 'Морковь': 2},
           'Сидоров': {'Макулатура': 1, 'Металлолом': 1, 'Морковь': 3},
           'Алексеева': {'Макулатура': 1, 'Металлолом': 2, 'Морковь': 8},
           'Джонсон': {'Макулатура': 23, 'Металлолом': 5, 'Морковь': 2}}

f = open('NewResults3.txt', encoding = 'utf-8')

for line in f:
    if line.find('-') == -1:
        collect = line.strip()
    else:
        words = line.split()
        person = words[0].strip()
        amount = int(words[2])
        if person not in results:
              results[person] = {}
        if collect in results[person]:
            results[person][collect] += amount
        else:
            results[person][collect] = amount
        
f.close()

pprint(results)

carrots = 0
paper = 0
best_pioneer = 0
metal = 0
k = 0
strange_pioneer = []
l = 0
provident_pioneer = 0
for pioneer, achievement in results.items():
    if 'Морковь' in achievement:
        carrots += achievement['Морковь']
    if 'Макулатура' in achievement:
        if achievement['Макулатура'] > paper:
            paper = achievement['Макулатура']
            best_pioneer = pioneer
    if 'Металлолом' in achievement:
        metal += achievement['Металлолом']
        k += 1
    if 'Странные предметы' in achievement:
        strange_pioneer.append(pioneer)
    p = 0
    for material in achievement:
        p += 1
        if p > l:
            l = p
            provident_pioneer = pioneer

print('Всего моркови: ', carrots)
print(f'Больше всего макулатуры собрал: {best_pioneer}, а именно {paper}')
print('Средний объём сбора металлолома на человека: ', metal/k)
print('Странные предметы собирали: ', strange_pioneer)
print('Больше всего предметов собирал: ', provident_pioneer)
