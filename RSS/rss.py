import requests
from bs4 import BeautifulSoup

r1 = requests.get('https://www.fontanka.ru/fontanka.rss')

if r1.status_code != 200:
    print('Эта страница не загрузилась!')

soup1 = BeautifulSoup(r1.content, features = "html.parser")

items = soup1.find_all('item')

#print('Всего элементов:', len(items))
#print(items[0])

with open('fontanka.txt', 'w') as f:
    for item in items:
        category = item.find('category')
        if category.text == 'Город':
            title = item.find('title')
            f.write(f'{title.text}\n')
            #print(title.text)
            link = item.find('pdalink')
            f.write(f'{link.text}\n')
            #print(link.text)
            f.write(f'\n')
            #print()
