from pprint import pprint

results = {'Иванова': {'Макулатура': 3, 'Металлолом': 1, 'Морковь': 4},
           'Петров': {'Макулатура': 10, 'Металлолом': 12, 'Морковь': 2},
           'Сидоров': {'Макулатура': 1, 'Металлолом': 1, 'Морковь': 3},
           'Алексеева': {'Макулатура': 1, 'Металлолом': 2, 'Морковь': 8},
           'Джонсон': {'Макулатура': 23, 'Металлолом': 5, 'Морковь': 2}}

f = open('NewResults0.txt', encoding = 'utf-8')

for line in f:
    words = line.split()
    person = words[0].strip()
    collect = words[1].strip()
    amount = int(words[2])
    results[person][collect] += amount

f.close()

pprint(results)
