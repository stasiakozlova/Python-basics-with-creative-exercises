import requests
from bs4 import BeautifulSoup

r = requests.post('https://www.kommersant.ru/archive/news?from=news')
print(r.status_code)
print(r.content)

soup = BeautifulSoup(r.content)
news = soup.findAll('li', {'class':'b-newsline__item'})
link = news[0].find('a', href=True)['href']
print(link)

base_link = 'https://www.kommersant.ru'
first_news = requests.post(base_link + link)
first_news_soup = BeautifulSoup(first_news.content)
article = first_news_soup.findAll('p', {'class':'b-article__text'})
print(article)
print(article[0].text)
print(article[4].text)

