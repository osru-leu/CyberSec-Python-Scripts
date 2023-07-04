import requests #requesting info from website
from bs4 import BeautifulSoup as bs

'''use .text to get the specific text of the html page. otherwise you'll just get a code 200 return'''
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup = bs(html_text, 'html.parser')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name').text
print(company_name)

