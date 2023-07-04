'''
loop through the pages

grab every 3rd article
by appending everything to lists 
'''

from bs4 import BeautifulSoup as bs
import requests
'''
the below code is not iterating through the pages
 '''

URL = 'http://www.geeksforgeeks.org/'
web_page = 0
for page in range(1, 6436, 1000):
    
    html_text = requests.get(URL).text
    soup = bs(html_text, 'lxml')

    tags = soup.find_all('div', class_ = 'articles-list_item')
    web_page += 1
    print('The web page number-_*_*_*_*_*_*_*_*_*_*_*', web_page, end='\n')
    '''Iterate through each article tag and '''
    article = 0
    for tag in tags:   
        title = tag.find('div', class_='head').text
        links = tag.find('a')['href']
        date_link = requests.get(links).text
        new_soup = bs(date_link, 'lxml')
        last_updated = new_soup.find('div', class_ = 'media').text
        article += 1
       
        print(title,'------->', links, 'article: ', article, last_updated, end='\n')
        print('---------------------------------------------------')