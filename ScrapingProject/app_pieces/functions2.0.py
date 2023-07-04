import requests
from bs4 import BeautifulSoup as bs


def get_link(url):
    ''''''
    link_for_bs = requests.get(url).text
    return link_for_bs


def soup_instance(link):  
    """in case of AttributeError: 'str' object has no attribute 'text'"""
    try:
        soup = bs(link.text, 'html.parser')
    except AttributeError:
        print('In except-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        soup = bs(link, 'html.parser')
    return soup


# def get_articles(url):
   


def find_title(url):
    '''Itertate through specified url pages and return the 3rd article'''
    for page in range(1000, 7000, 1000):
        # print(page)
        page_req = requests.get(url + '/page/' + str(page) + '/')
        soup_return = soup_instance(page_req)
        articles = soup_return.find_all('div', class_ = 'articles-list_item')[2]
        # return articles
        for tag in articles:
            read_more = articles.find('a')['href']
            link_info = get_link(read_more)
            soup = soup_instance(link_info)
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
# NOTE REDUNDANT:?
# def find_all_tags(soup, tag:str, class_:str, indx:None):
#     tags = soup.find_all(tag, class_)[indx]
#     return tags


# TESTS
# get_link and soup_instance test:
URL = 'https://www.geeksforgeeks.org'
# print(soup_instance(get_link(URL)))
soup = soup_instance(get_link(URL))
# articles = find_all_tags(soup, 'div', 'articles-list_item', 2)
# print(articles.text)
print(soup.text)
# articles = get_articles(URL)
# print(articles.text)
# title = find_title(articles)
# print(title)