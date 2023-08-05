# rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя 1234567890,.-;&!'

original_text = input('Что дешифровать? ')
final_text = ''

for letter in original_text:
    old_position = rus_alphabet.find(letter)
    new_position = (old_position - 4) % 83
    new_letter = rus_alphabet[new_position]
    final_text = final_text + new_letter

print(final_text)
