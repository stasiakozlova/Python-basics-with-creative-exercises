class Backpack:
    """ Рюкзак """

    def __init__(self, gift = None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __len__(self):
        return len(self.content)

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        new_obj.content.extend(other.content)
        return new_obj

    def __sub__(self, other):
        new_obj = Backpack()
        new_obj.content = self.content
        for item2 in other.content:
            if item2 in new_obj.content:
                new_obj.content.remove(item2)
        return new_obj

    def __bool__(self):
        return self.content != []

    def add(self, item = 'конфета'):
        """ Положить в рюкзак """
        self.content.append(item)
        print('В рюкзак положили:', item)

    def inspect(self):
        """ Проверить содержимое """
        print('В рюкзаке лежит:')
        for item in self.content:
            print(' ', item)

print('Взрослый рюкзак:')
my_backpack = Backpack(gift = 'фонарик')
my_backpack.add(item = 'ноутбук')
my_backpack.add(item = 'зарядка для ноутбука')
my_backpack.add()
my_backpack.inspect()
if my_backpack:
    print('Рюкзак не пустой!')
print('Количество предметов в рюкзаке:', len(my_backpack))

print('\nДетский рюкзак:')
kid_backpack = Backpack(gift = 'банан')
kid_backpack.add(item = 'фонарик')
kid_backpack.inspect()

new_backpack = my_backpack + kid_backpack
print('\nНовый рюкзак-сложение (что есть в обоих рюкзаках):')
new_backpack.inspect()

new_backpack_2 = my_backpack - kid_backpack
print('\nНовый рюкзак-вычитание (что есть только во взрослом рюкзаке):')
new_backpack_2.inspect()

