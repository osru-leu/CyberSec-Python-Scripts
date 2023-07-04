
import requests
from bs4 import BeautifulSoup as bs


def get_link(url):
    ''''''
    link_for_bs = requests.get(url)
    return link_for_bs


def soup_instance(url):  
    """in case of AttributeError: 'str' object has no attribute 'text'"""
    link = requests.get(url)
    soup = bs(link.text, 'html.parser')
    # try:
    #     soup = bs(link.text, 'html.parser')
    # except AttributeError as err:
    #     print(err, 'In except-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    #     soup = bs(link, 'html.parser')
    return soup


def get_articles(url):#use this to iterate pages 
    '''Itertate through specified url page and return the 3rd article'''
    for page in range(1000, 7000, 1000):
     
        page_req = requests.get(url + '/page/' + str(page) + '/')
        # soup_return = soup_instance(page_req)
        soup = bs(page_req.text, 'html.parser')
        articles = soup.find_all('div', class_ = 'articles-list_item')[2]
        # articles = soup_return.find_all('div', class_ = 'articles-list_item')[2]
     
        for tag in articles:
            read_more = articles.find('a')['href']
            link_info = get_link(read_more).text
            soup = bs(link_info, 'html.parser')
            title = articles.find('a')['title']
            return title[13:]


def find_date(strong_list):

    for element in strong_list:
        if element.text == 'Last Updated :':
            date = element.next_element.next_element.next_element.text
        return date

'''
TODO string functs together for testing
    - make a grab single title function? and date?
        -solve the single date issue
    -display page?
'''

# TESTS
# get_link and soup_instance test:
URL = 'https://www.geeksforgeeks.org'
# print(soup_instance(get_link(URL)))
# url = get_link(URL)
# print(url)
soup = soup_instance(URL)
print(soup)
# articles = find_all_tags(soup, 'div', 'articles-list_item', 2)
# print(articles.text)

arts = get_articles(soup)
print(arts)
 #TODO why am i not getting only one title when calling get_articles?