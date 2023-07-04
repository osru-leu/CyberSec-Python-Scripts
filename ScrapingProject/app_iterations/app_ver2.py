
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
# print('Page: 1','---->', article.text, updated.text)
first_title = article.find('a')['title']
print(first_title[13:], updated.text)

    
for page in range(1000, 7000, 1000):
    page_req = requests.get(URL + '/page/' + str(page) + '/')
    soup_2 = bs(page_req.text, 'html.parser')
    articles = soup_2.find_all('div', class_ = 'articles-list_item')[2]# 2 times repeated
    
    for tag in articles:
        rm_link = articles.find('a')['href'] # 2 times repeated a funct?
        link_info = requests.get(rm_link).text # 4 times repeated
        soup_3 = bs(link_info, 'html.parser') # 3 times repeated
        # last_updated = soup_3.find('div', class_ = 'media')NOTE no longer needed
        strong_list = soup_3.find_all('span', class_='strong')
        title = articles.find('a')['title']
        ''' strong filter - filter out difficulty level '''    
        for i in strong_list:
            if i.text == 'Last Updated :':
                date = i.next_element.next_element.next_element.text
               
        
        print('Page:', page, '---->', title[13:],'<->', 'Last Updated:', date)

"""

TODO and CONSIDERATIONS
    put the first_title throught the 'strong filter """