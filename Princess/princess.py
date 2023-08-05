names = set()
father = ["Abigail", "Adaline", "Adelaide", "Adele", "Albertina", "Alethea", "Ophelia"]
mother = ["Abigail", "Alexandra", "Augusta", "Louise", "Frederica", "Sophie", "Henrietta", "Amelia", "Theresa"]
grandfather = ["A", "O", "E", "V", "B"]
final = []

#Множество имён британских принцесс
with open('princess.txt', 'r') as f:
    for line in f:
        names.update(line.split())

#Множество имён, которые нравятся папе
father_names = set(father)
#Множество имён, которые не нравятся маме
mother_stop = set(mother)
#Множество букв, которые нравятся дедушке
grandfather_letters = set(grandfather)
#Преобразую final_names в множество
final_names = set(final)

#Добавляю в names множество папы
names.update(father_names)
#Вычитаю из names множество мамы
names -= mother_stop
#Отбираю имена с дедушкиными буквами
for name in names:
    if name[0] in grandfather_letters:
        final_names.add(name)

final_names_string = ', '.join(final_names)
print(f'Уважаемая богатая британская семья, вот список подходящих имён для Вашей чудесной дочери: {final_names_string}')
