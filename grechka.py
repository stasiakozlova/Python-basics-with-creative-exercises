def check_food(food_name, amnt):
    if food[food_name] >= amnt:
        food[food_name] -= amnt
    else:
        print('Продукт отсутсвует: ', food_name)

def giving(dict_name, message):
    for food_dict, amnt_dict in dict_name.items():
        check_food(food_name = food_dict, amnt = amnt_dict)
    print(message)

food = {'Гречка(пачки)': 1, 'Шпроты(банки)': 4, 'Салями(палки)': 4, 'Горошек(банки)': 4,
        'Икра красная(банки)': 2}

profkom = {'Гречка(пачки)': 1, 'Шпроты(банки)': 1, 'Салями(палки)': 1, 'Горошек(банки)': 2}
supplier = {'Гречка(пачки)': -30, 'Шпроты(банки)': -30, 'Салями(палки)': -30, 'Горошек(банки)': -60,
        'Икра красная(банки)': -2}
step_step = {'Гречка(пачки)': 1, 'Шпроты(банки)': 1, 'Салями(палки)': 1, 'Горошек(банки)': 2,
        'Икра красная(банки)': 2}

while True: 
    name = input('Введите фамилию: ')
    if name == 'сторож':
        print('Стол заказов закрыт', 'Оставшиеся продукты:', food)
        break
    elif name in ['Иванова', 'Петров', 'Сидоров']:
        giving(profkom, 'Заберите свой заказ')
    elif name == 'Поставщик':
        giving(profkom, 'продукты добавлены')
    elif name == 'Степан Степаныч':
        giving(step_step, 'продукты добавлены')
        for food_dict, amnt_dict in step_step.items():
            check_food(food_name = food_dict, amnt = amnt_dict)
        print('Приходите ещё, Степан Степанович!')
