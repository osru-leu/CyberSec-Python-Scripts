import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.geeksforgeeks.org'
base_url = requests.get(URL)
soup_1 = bs(base_url.text, 'html.parser')
first_title = soup_1.find_all('div', class_ = 'articles-list_item')[2].text
print(first_title)



title = first_title.find('div', class_='head').text
links = first_title.find('a')['href']
link_info = requests.get(links).text
soup_3 = bs(link_info, 'html.parser')
last_updated = soup_3.find('div', class_ = 'media').text
print(last_updated)