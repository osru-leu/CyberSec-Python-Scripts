import requests 
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org'
html_text = requests.get(URL).text
soup = bs(html_text, 'html.parser')

tag = soup.find_all('div', class_ = 'articles-list_item')[2]
# print(tag.text)

title = tag.find('div', class_ = 'head').text # FOR PRINTING PURPOSES ONLY
# print(title)
links = tag.find('a')['href']

search_link = requests.get(links).text
new_soup = bs(search_link, 'html.parser')

last_updated = new_soup.find('div', class_ = 'media').text
print(title, last_updated)