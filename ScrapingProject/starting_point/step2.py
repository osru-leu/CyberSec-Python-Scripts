'''
loop through each article title and grab all of the "last updated" dates for each title 
'''

from bs4 import BeautifulSoup as bs
import requests

'''
grab every article title and "last updated" date'''

URL = 'http://www.geeksforgeeks.org/'
web_page = 0
  
html_text = requests.get(URL).text
soup = bs(html_text, 'lxml')

tags = soup.find_all('div', class_ = 'articles-list_item')
web_page += 1
print('The web page number-_*_*_*_*_*_*_*_*_*_*_*', web_page, end='\n')

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
       
    


'''
'''
#NOTE reference link for scraping multiple pages
# https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-of-a-website-using-python/
