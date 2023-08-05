import random

responses_hello = ['Здравствуй, человек!', 'Здравствуй!', 'Приветствую тебя, человек!', 'Говори']
responses_goodbye = ['Пока!', 'Всего хорошего!', 'Бывай!', 'Земля круглая, может ещё встретимся']

print('Бот готов к работе!')

while True:
    question = input()
    if question == 'выход':
        break
    elif question in ['привет', 'Привет', 'здравствуй', 'Здравствуй', 'здравствуйте', 'Здравствуйте']:
        answer = random.choice(responses_hello)
    elif question in ['До свидания', 'до свидания', 'Пока', 'пока', 'Adieu', 'adieu', 'Ciao', 'ciao']:
        answer = random.choice(responses_goodbye)
    else:
        answer = question
    print(answer)
