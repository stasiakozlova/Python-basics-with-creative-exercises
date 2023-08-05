import requests
from bs4 import BeautifulSoup

r = requests.post('https://gorod-812.ru/category/d0-b0-d1-80-d1-85-d0-b8-d1-82-d0-b5-d0-ba-d1-82-d1-83-d1-80-d0-b0/')

if r.status_code != 200:
    print('Что-то пошло не так!')

soup = BeautifulSoup(r.content, features="html.parser")

articles = soup.find_all('article')

print(len(articles))
print(articles[0])

spb_file = open('spb.txt', 'w')

for article in articles:
    a = article.find('a')
    current_url = a['href']
    print(current_url)
    r2 = requests.post(a['href'])
    soup2 = BeautifulSoup(r2.content, features="html.parser")
    paragraphs = soup2.find_all('p')
    for paragraph in paragraphs:
        if len(paragraph.text.strip()) == 0:
            break
        if 'Теги:' in paragraph.text:
            break
        spb_file.write(paragraph.text)
        spb_file.write('\n')

spb_file.close()

