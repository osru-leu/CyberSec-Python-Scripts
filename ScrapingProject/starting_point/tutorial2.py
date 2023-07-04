'''
Steps:
-import all necessary libraries
-set up our URL strings for making a connection using the requests
library
-from the target page, identify and Extract the classes and tags
which contain the information that is valuable to us
-prototype it for one page using a loop and then apply it to all the 
pages.

'''
# Async the below code 
# replicate it but make minor changes to look for something else
# run both as async defs

import asyncio 
import requests
from bs4 import BeautifulSoup as bs


async def find_titles():

    for page in range(1, 10):
        URL = 'https://www.geeksforgeeks.org/page/'
        req = requests.get(URL + str(page) + '/')
        # print(req)
        
        soup = bs(req.text, 'html.parser')
        titles = soup.find_all('div', attrs = {'class', 'head'})#NOTE use this for something else

        for i in range(4, 19):
            if page > 1:
                print(f'{(i - 3) + page * 15}' + titles[i].text)
                await asyncio.sleep(0)    
            else:
                print(f'{i - 3}' + titles[i].text)

        
async def get_scripts():
    
    URL = 'https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-of-a-website-using-python/'
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    scripts = soup.find('script', text=True)
    print(scripts)


async def main():
    funct1 = loop.create_task(find_titles())
    funct2 = loop.create_task(get_scripts())
    await asyncio.wait([funct1, funct2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# grab_titles = asyncio.gather(find_titles())
# grab_script = asyncio.gather(get_scripts())

# grab_all = asyncio.gather(grab_titles, grab_script)

# result = loop.run_until_complete(grab_all)
# loop.close()

