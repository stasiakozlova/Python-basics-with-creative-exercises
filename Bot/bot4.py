import random

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['привет', 'здравствуй', 'приветствую',],
            'responses': ['Здравствуй, человек!', 'Здравствуйте!', 'Приветствую, человек!',],
            },
        'bye': {
            'examples': ['пока', 'до свидания', 'спасибо вам',],
            'responses': ['До свидания!', 'Пока!', 'Всего хорошего!',]
            }
        },
    'failure_phrases': ['Извините, я не понял', 'Пожалуйста, сформулируйте иначе', 'Я не понимаю']
    }

def filter_text(text):
    text = text.lower()
    deletechars = '.,:*?!"<>'
    for c in deletechars:
        text = text.replace(c, '')
    return text

def get_intent(question):
    question = filter_text(question)
    for intent, intent_data in BOT_CONFIG['intents'].items():
        #for example in intent_data['examples']:
        if question in intent_data['examples']:
            return intent
    else:
        return None

def get_answer_by_intent(intent):        
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases)

def get_failure_phrase():
    answer = random.choice(BOT_CONFIG['failure_phrases'])
    return answer

def bot(question):
    intent = get_intent(question)
    if intent:
        answer = get_answer_by_intent(intent)
    else:
        answer = get_failure_phrase()
    return answer

print('Бот готов к работе!')

while True: 
    question = input()
    if question == 'выход':
        break
    answer = bot(question)
    print(answer)
