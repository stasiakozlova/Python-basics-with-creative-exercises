from random import randint

class Man:
    '''Виртуальный человек'''

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        self.energy = 30
        self.concert_times = 0
        self.eat_times = 0
        self.play_instrument_times = 0
        self.shopping_times = 0
        self.tidy_up_times = 0

    def __str__(self):
        return f'Я - {self.name}, энергия - {self.energy}.'

    def concert(self):
        print(f'{self.name} сыграл концерт и получил за него деньги.')
        self.concert_times += 1
        home.money += 50
        self.energy -= 10

    def eat(self):
        if home.food >= 10:
            print(f'{self.name} поел.')
            self.eat_times += 1
            self.energy += 10
            home.food -= 10
        else:
            print('Нет еды!')

    def shopping(self):
        if home.money >= 10:
            print(f'{self.name} сходил в магазин.')
            self.shopping_times += 1
            home.money -= 10
            home.food += 20
            self.energy -= 10
        else:
            print('Нет денег!')

    def play_instrument(self):
        print(f'{self.name} поиграл на {self.instrument}.')
        self.play_instrument_times += 1
        self.energy -= 10

    def tidy_up(self):
        print(f'{self.name} прибрался в квартире.')
        self.tidy_up_times += 1
        home.dirt -= 50
        self.energy <= 20

    def act(self):
        if self.energy <= 0:
            print(f'{self.name} уехал в санаторий.')
        dice = randint(1, 6)
        if self.energy <= 20:
            self.eat()
        elif home.money <= 10:
            self.concert()
        elif home.food <= 20:
            self.shopping()
        elif home.dirt >= 50:
            self.tidy_up()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.concert()
        else:
            self.play_instrument()

    def print_year_results(self):
        return f'{self.name} сыграл концерт {self.concert_times} раз, сходил в магазин {self.shopping_times} раз, '\
               f'играл на {self.instrument} {self.play_instrument_times} раз, ел {self.eat_times} раз, прибирался {self.tidy_up_times} раз.'

class Cat:
    '''Виртуальный кот'''

    def __init__(self, name):
        self.name = name
        self.energy = 20
        self.sleep_times = 0
        self.eat_times = 0
        self.play_times = 0

    def __str__(self):
        return f'Я - кот {self.name}, энергия - {self.energy}.'

    def sleep(self):
        print(f'Кот {self.name} поспал.')
        self.sleep_times += 1
        self.energy -= 5
        
    def eat(self):
        print(f'Кот {self.name} поел.')
        self.eat_times += 1
        self.energy += 20
        home.food -= 10
        
    def play(self):
        print(f'Кот {self.name} подрал обои.')
        self.play_times += 1
        self.energy -= 10
        home.dirt += 5

    def act(self):
        if self.energy <= 0:
            print(f'Кот {self.name} ушёл жить к более успешным хозяевам.')
        dice = randint(1, 6)
        if self.energy <= 20:
            self.eat()
        elif dice < 4:
            self.sleep()
        else:
            self.play()

    def print_year_results(self):
        return f'Кот {self.name} поспал {self.sleep_times} раз, поел {self.eat_times} раз, подрал обои {self.play_times} раз.'

class Home:
    '''Виртуальный дом'''

    def __init__(self):
        self.food = 10
        self.money = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме: еды - {self.food}, денег - {self.money}, грязи - {self.dirt}.'

  
nick = Man('Никола Николаич', 'барабанах')
andrew = Man('Андрюша Квака', 'гитаре')
dan = Man('Даниил Романович', 'басу')
home = Home()
barsik = Cat('Барсик')
entrecote = Cat('Антрекот')

for day in range (1, 365):
    print(f'============ день {day} ============')
    nick.act()
    andrew.act()
    dan.act()
    barsik.act()
    entrecote.act()
    print(nick)
    print(andrew)
    print(dan)
    print(barsik)
    print(home)

print(nick.print_year_results())
print(andrew.print_year_results())
print(dan.print_year_results())
print(barsik.print_year_results())
print(entrecote.print_year_results())
