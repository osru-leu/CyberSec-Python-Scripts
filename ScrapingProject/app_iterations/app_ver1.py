
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org'
base_url = requests.get(URL)
soup = bs(base_url.text, 'html.parser')
article = soup.find_all('div', class_ = 'articles-list_item')[2]
read_more = article.find('a')['href']
link = requests.get(read_more)
soup_1 = bs(link.text, 'html.parser')
updated = soup_1.find('div', class_ = 'media')
print('1 ---->', article.text, updated.text)

    
for page in range(1000, 7000, 1000):
    page_req = requests.get(URL + '/page/' + str(page) + '/')
    soup_2 = bs(page_req.text, 'html.parser')
    articles = soup_2.find_all('div', class_ = 'articles-list_item')[2]

    for tag in articles:
        rm_link = articles.find('a')['href']
        link_info = requests.get(rm_link).text
        soup_3 = bs(link_info, 'html.parser')
        last_updated = soup_3.find('div', class_ = 'media').text

        print(page, '---->', tag.text, last_updated)

