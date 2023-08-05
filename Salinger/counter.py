from collections import Counter

c1 = Counter()

with open('salinger.txt', 'r') as f:
    for line in f:
        line_items = line.lower().strip().split()
        for token in line_items:
            cleaned_token = token.strip('.,"!?-()\'\/')
            c1[cleaned_token] += 1

with open('frq1.txt', 'w') as f2:
    for item in sorted(c1):
        f2.write(f'{item}\t\t{c1[item]}\n')

print('Готово!')
