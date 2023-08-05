current_hour = 8
current_minute = 3

question1 = input('Скажите, пожалуйста, как Вас зовут? ')
question2 = int(input('Сколько Вам лет? '))

#Первый вариант задачи, со "Здравствуйте" для средних
#if question2 < 18:
#    print('Привет,', question1)
#elif 18 <= question2 <= 65:
#    print('Здравствуйте,', question1)
#else:
#    print('Сердечно приветствую Вас,', question1)

#Второй вариант задачи, с ветвлением для средних
if question2 < 18:
    print('Привет,', question1)
elif 18 <= question2 <= 65:
    if 4 <= current_hour <= 11:
        print('Доброе утро,', question1)
    elif 11 < current_hour <= 16:
        print('Добрый день,', question1)
    elif 16 < current_hour <= 23:
        print('Добрый вечер,', question1)
    else:
        print('Доброй ночи,', question1)
else:
    print('Сердечно приветствую Вас,', question1)

if current_hour in [1, 21]:
    hour_ending = ''
elif current_hour in [2, 3, 4, 22, 23, 24]:
    hour_ending = 'а'
else:
    hour_ending = 'ов'

if current_minute in [1, 21, 31, 41, 51]:
    minute_ending = 'а'
elif current_minute in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]:
    minute_ending = 'ы'
else:
    minute_ending = ''
    
print('Сейчас', current_hour, 'час' + hour_ending, current_minute, 'минут' + minute_ending + '!')
