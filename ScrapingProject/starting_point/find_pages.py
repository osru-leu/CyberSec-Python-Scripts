
'''for later reference: 
https://www.youtube.com/watch?v=4VfqVpTz4Q4
https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-of-a-website-using-python/'''

'''NOTE can i just get the page box and iterate through it and if else the
ending page class?'''


import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.geeksforgeeks.org'
html_text = requests.get(URL).text

soup = bs(html_text, 'lxml')
tag = soup.find('div', class_ = 'articles-list_item')

pages = soup.find('div', class_ = 'wp-pagenavi').text #pagination tag




print(pages)
# all = pages.find('a')['href']
# print(all)

   
'''find the pagination list name
    -find the next button
        -if this element is not on the page'''