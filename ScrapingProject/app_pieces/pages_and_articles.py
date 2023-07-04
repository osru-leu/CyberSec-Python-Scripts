'''Grab Every 3rd article title on every 1000th page'''
#NOTE retype do what you can from memory just cause*************************************************************************
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org'
base_url = requests.get(URL)
soup_1 = bs(base_url.text, 'html.parser')
first_title_plus = soup_1.find_all('div', class_ = 'articles-list_item')[2].text
print(first_title_plus)

for page in range(1000, 7000, 1000):
    '''-for each 1000th page up to 7000 get all article titles
    -concatenate the requested url using pagination '''

    page_req = requests.get(URL + '/page/' + str(page) + '/')
    soup_2 = bs(page_req.text, 'html.parser')
    articles = soup_2.find_all('div', class_='articles-list_item')

    links = soup_2.find('a')['href']
    print(links)

    title = soup_2.find_all('div', class_ = 'head')
    print(title)

    # for article in range(2, 3):
    #     '''for all articles get the third title'''
    #     print(page, articles[article].text) #NOTE orignal code

        
        # get_link_info = requests.get(links).text
        # soup_3 = bs(get_link_info, 'html.parser')
        # last_updated = soup_3.find('div', class_ = 'media').text
        # print(last_updated)
       


'''
Determine if there is a need for the second for loop because you can use list
indexing to to grab the article you need Ex:
first_title = soup_1.find_all('div', class_ = 'articles-list_item')[2].text
turn articles var to:
articles = soup_2.find_all('div', class_ = 'articles-list_item')[2].text

'''