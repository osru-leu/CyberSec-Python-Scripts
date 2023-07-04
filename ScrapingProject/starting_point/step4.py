'''
Make functions out of given code
'''

import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    url = requests.get(url)
    soup = bs(url.text, 'html.parser')
    return soup


'''Messy Trace back and correct then decide if necessary-does this need to be a function?'''
def get_articles(url):
    for page in range(1000, 7000, 1000):
        page_req = requests.get(url + '/page/' + str(page) + '/')
        soup = get_soup(url)
        articles = soup.find_all('div', class_ = 'articles-list_item')[2].text
        
        return articles



if __name__=='__main__':
    URL = 'https://www.geeksforgeeks.org'
    # get_soup(URL)
    print(get_articles(URL))
    