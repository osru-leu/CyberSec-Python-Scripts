
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org'
base_url = requests.get(URL)
soup_1 = bs(base_url.text, 'html.parser')
first_title = soup_1.find_all('div', class_ = 'articles-list_item')[2].text
print('1', first_title)

for page in range(1000, 7000, 1000):
    '''-for each 1000th page up to 7000 get all article titles
    -concatenate the requested url using pagination '''

    page_req = requests.get(URL + '/page/' + str(page) + '/')
    soup_2 = bs(page_req.text, 'lxml')
    articles = soup_2.find_all('div', class_='articles-list_item')[2].text
    # title = article.find('div', class_='head').text
    print(page, articles)
    
    # for article in articles:
        
    #     title = article.find('div', class_='head').text
    #     links = article.find('a')['href']
    #     link_info = requests.get(links).text
    #     soup_3 = bs(link_info, 'html.parser')
    #     last_updated = soup_3.find('div', class_ = 'media').text
    #     print(last_updated)
        
    # title = articles.find_all('div', class_ = 'head').text

    # for article in range(2, 3):
    #     '''for all articles get the third title'''
    #     # print(page, articles[article].text) #NOTE orignal code

        
    #     get_link_info = requests.get(links).text
    #     soup_3 = bs(get_link_info, 'html.parser')
    #     last_updated = soup_3.find('div', class_ = 'media').text
    #     print(last_updated)
        
