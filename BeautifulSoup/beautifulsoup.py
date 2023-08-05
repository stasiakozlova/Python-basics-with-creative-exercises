import requests
from bs4 import BeautifulSoup

r = requests.post('https://www.kommersant.ru/archive/news?from=news')
print(r.status_code)
print(r.content)
soup = BeautifulSoup(r.content, features="html.parser")
#print(soup)
news = soup.findAll('div', {'class':'uho__text rubric_lenta__item_text'})
link = news[0].find('a', href=True)['href']
base_link = 'https://www.kommersant.ru'
first_news = requests.post(base_link + link)
first_news_soup = BeautifulSoup(first_news.content, features="html.parser")
article = first_news_soup.findAll('div', {'itemprop':'articlebody'})

#print(first_news_soup)
#print(link)
#print(news[-1])

