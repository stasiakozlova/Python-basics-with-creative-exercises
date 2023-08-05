class Bird:
    '''Виртуальная птица'''

    def __init__(self):
        print('Появилась ещё одна птица!')
        self.color = 'черепаший'
        self.size = 'небольшой'

    def talk(self):
        print('Чик-чирик!')

class Cow:
    '''Виртуальная корова'''

    def __init__(self, name):
        self.name = name
        print('Появилась ещё одна корова:', self.name + '!')
        self.color = 'бурый'
        self.size = 'большой'

    def __str__(self):
        return f'Это - корова. Имя - {self.name}, цвет - {self.color}.'

    def talk(self):
        print('Мууу-уу!')

cow1 = Cow('Бурёнка')
cow1.talk()
cow2 = Cow('Зорька')
cow1.talk()

print(cow2)

bird1 = Bird()
bird2 = Bird()

bird1.talk()
bird2.talk()

print('Цвет:', bird2.color)
print('Размер:', bird2.size)
