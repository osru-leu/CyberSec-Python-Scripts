
'''Grabs the titles and the "read more" links of those titles, of the first page'''
from bs4 import BeautifulSoup
import requests


URL = 'http://www.geeksforgeeks.org/'
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'lxml')#NOTE poss prob

tags = soup.find_all('div', class_ = 'articles-list_item')


for tag in tags:   
    title = tag.find('div', class_='head').text
    links = tag.find('a')['href']
    link_info = requests.get(links).text
    new_soup = BeautifulSoup(link_info, 'html.parser')
    last_updated = new_soup.find('div', class_ = 'media').text
    print(title,'--------> ', last_updated)
    
    

