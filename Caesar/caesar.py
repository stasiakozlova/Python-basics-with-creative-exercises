rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя 1234567890,.-;&!'

def caesar(operation, original_text):
    final_text = ''
    if operation == 'зашифровать':
        for letter in original_text:
            old_position = rus_alphabet.find(letter)
            new_position = (old_position + 4) % 83
            new_letter = rus_alphabet[new_position]
            final_text = final_text + new_letter
    else:
        for letter in original_text:
            old_position = rus_alphabet.find(letter)
            new_position = (old_position - 4) % 83
            new_letter = rus_alphabet[new_position]
            final_text = final_text + new_letter
    return final_text

while True:
    operation = input('Зашифровать или дешифровать? ')
    original_text = input('Введите фразу: ')
    final_text = caesar(operation, original_text)
    print(final_text)
    question = input('Хотите продолжить? ')
    if question == 'нет':
        break
