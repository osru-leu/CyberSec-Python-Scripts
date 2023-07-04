'''
Through a URL search on geeksforgeeks.org, get the href tag link to read more..., then get the "last updated: date"
from that URL.'''

import requests
from bs4 import BeautifulSoup as bs

URL = 'http://www.geeksforgeeks.org'
html_text = requests.get(URL).text

soup = bs(html_text, 'lxml')
tag = soup.find('div', class_ = 'articles-list_item')

title = tag.find('div', class_ = 'head').text
SECOND_URL = tag.find('a')['href']

sec_html_text = requests.get(SECOND_URL).text
new_soup = bs(sec_html_text, 'lxml')

last_updated = new_soup.find('div', class_ = 'media').text
print(last_updated)

