crew = 'Наша команда: '
while True:
    print('Познакомимся с новым членом команды.')
    name = str(input('Как Вас зовут? '))
    print('Здравствуйте,', name + '!')
    crew = crew + name + ', '
    if name == 'Паганель':
        break
final_crew = crew[:-2] + '.'
print(final_crew)
