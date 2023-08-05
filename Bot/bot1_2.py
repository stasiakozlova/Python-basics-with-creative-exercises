import random

questions_hello = ['привет', 'здравствуй', 'здравствуйте']
questions_goodbye = ['до свидания', 'пока', 'adieu', 'ciao']
responses_hello = ['Здравствуй, человек!', 'Здравствуй!', 'Приветствую тебя, человек!', 'Говори']
responses_goodbye = ['Пока!', 'Всего хорошего!', 'Бывай!', 'Земля круглая, может ещё встретимся']
failure_phrases = ['Извините, я Вас не понял.', 'Не понимаю, что Вы говорите.', 'Мне трудно понять Вас.']

def filter_text(text):
    text = text.lower()
    deletechars = '.,:*?!"<>|'
    for c in deletechars:
        text = text.replace(c, '')
    return text

def get_intent(question):
    question = filter_text(question)
    if question in questions_hello:
        intent =  'hello'
    elif question in questions_goodbye:
        intent = 'bye'
    else:
        intent = None
    return intent

def get_answer_by_intent(intent):
    if intent == 'hello':
        answer = random.choice(responses_hello)
    elif intent == 'bye':
        answer = random.choice(responses_goodbye)
    else:
        answer = random.choice(failure_phrases)
    return answer
        
def bot(question):
    intent = get_intent(question)
    answer = get_answer_by_intent(intent)
    return answer
    
print('Бот готов к работе!')

while True:
    question = input()
    if question == 'выход':
        break
    answer = bot(question)
    print(answer)
