crew = 'Наша команда: '
i = 1
for i in range(1, 6):
    print('Познакомимся с новым членом команды.')
    name = str(input('Как Вас зовут? '))
    print('Здравствуйте,', name + '!')
    crew = crew + name + ', '
    i = i + 1
final_crew = crew[:-2] + '.'
print(final_crew)
