import requests

'''
1. Gather all href links
2. follow all links and repeat
    make a function:
        grab a link
        put link through get function
        return result
    for link in result:
        store link in list
        send link to the getFunct()
        REVALUATE WHAT TO DO FROM HERE'''
page = requests.get("https://learning.flatironschool.com/courses/6180/pages/net400-m1-1-videos-web-spiders-3-videos-total-time-26-22?module_item_id=476965")
# print(page.text)


def get_html(html):
    page = requests.get(html)
    return page.text


link = "https://learning.flatironschool.com/courses/6180/pages/net400-m1-1-videos-web-spiders-3-videos-total-time-26-22?module_item_id=476965"
print(get_html(link))
