animals = {'коровы': 2, 'козы': 4, 'курицы': 10, 'утки': 2, 'перепёлки': 15, 'кошки': 3, 'собаки': 2, 'морские свинки': 2}
animals_neighbour = {'козы': 2, 'курицы': 4, 'утки': 1, 'страусы': 2, 'шиншиллы': 1}

birds = ['курицы', 'утки', 'перепёлки', 'cтраусы']
pets = ['кошки', 'морские свинки', 'шиншиллы']

total_amount = 0
total_birds = 0
total_pets = 0
max_name = ""
max_amount = 0

for animal_neighbour, amount_neighbour in animals_neighbour.items():
    if animal_neighbour in animals:
        animals[animal_neighbour] += amount_neighbour
    else:
        animals[animal_neighbour] = amount_neighbour

for animal, amount in animals.items():
    total_amount = total_amount + amount
    if animal in birds:
        total_birds = total_birds + amount
    if animal in pets:
        total_pets = total_pets + amount
    if amount > max_amount:
        max_amount = amount
        max_name = animal
    print(animal, '-', amount)

print('\nВсего животных -', str(total_amount) + '.')
print('Всего птиц -', str(total_birds) + '.')
print('Всего домашних животных -', str(total_pets) + '.')
print('Самое частое животное -', max_name + '.', 'Их -', str(max_amount) + '.')
