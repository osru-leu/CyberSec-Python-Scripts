import requests
from bs4 import BeautifulSoup as bs

URL = 'http://www.geeksforgeeks.org/'
html_text = requests.get(URL).text
soup = bs(html_text, 'lxml')
tag = soup.find('div', class_ = 'articles-list_item')

title = tag.find('div', class_='head').text
links = tag.find('a')['href']
# print(title, '----------->', links)
#what do you need to find next?TODO <-----------------------------------TODO 
    # -first lets find SOMETHING in link TODO <-----------------------------------TODO 
# date = tag.find('article', class_ = 'content post-619670 post type-post status-publish format-standard hentry category-geometric category-mathematical tag-area-volume-programs')
# print(date)
srch_link = requests.get(links).text
new_soup = bs(srch_link, 'lxml')
last_updated = new_soup.find('div', class_='media').text
print(last_updated)
    #first just grab something from the url then trace it down
    # curr_html = requests.get(link).text
    # print(curr_html)

