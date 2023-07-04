'''
Date: Jun 2021
*NOTE:
    This code is vulnerable to the ongoing restructuring of the webite
    geeksforgeeks.com. Due to this, the program no longer functions properly as it did
    when it was written.
'''


import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org'


def get_request(url):
    link = requests.get(url)
    return link

def get_soup(link):
    try:
        soup = bs(link.text, 'html.parser')
    except AttributeError as err:
        soup = bs(link, 'html.parser')
    return soup

def remove_diff_lvl(strong_list):
    for i in strong_list:
        if i.text == 'Last Updated :':
            date = i.next_element.next_element.next_element.text
    return date

def iterate_pages(start, stop, step):
    for page in range(start, stop, step):
        page_req = get_request(URL + '/page/' + str(page) + '/')
        soup_2 = get_soup(page_req)
        articles = soup_2.find_all('div', class_ = 'articles-list_item')[2]
        for tag in articles:
            title = articles.find('a')['title']
            rm_link = articles.find('a')['href']
            link_info = get_request(rm_link)
            soup_3 = get_soup(link_info)
            strong_list = soup_3.find_all('span', class_ = 'strong')
            updated = remove_diff_lvl(strong_list)
            print(f'Page: {page}, Title: "{title[13:]}", Last Updated: {updated}')


if __name__ == '__main__':
    # request URL, instantiate BeautifulSoup parse html
    base_url = get_request(URL)
    soup = get_soup(base_url)

    # get third article of page 1, get title from third article of page 1
    article = soup.find_all('div', class_ = 'articles-list_item')[2]
    first_title = article.find('a')['title']

    # store read more link, request "read more" URL, instantiate BeautifulSoup on "read more" link
    read_more = article.find('a')['href']
    link = get_request(read_more)
    soup_1 = get_soup(link)
    
    #get last updated with difficulty level from "read more" link
    strng_list = soup_1.find_all('span', class_ = 'strong')
    
    # print first title and titles as well as last updated from first page and selected pages
    print(f'Page: 1, Title: "{first_title[13:]}", Last Updated: {remove_diff_lvl(strng_list)}')
    iterate_pages(1000, 7000, 1000)

    
