from selenium import webdriver
from bs4 import BeautifulSoup
import json 


URL = 'http://www.kfdn.co.kr/sub.html?section=sc5&section2=%EC%A0%95%EC%B1%85'
driver = webdriver.Chrome()
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.select(
    '.sub_read_list_box > dl > dt > a'
)

tag = soup.select('.sub_read_list_box > dl > .sbody> a')

for tag in soup.select('.sub_read_list_box > dl > .sbody> a'):
    if 'href' in tag.attrs:
        link = tag.attrs['href']
        print(link)

content = soup.select(
    '.sub_read_list_box > dl > .sbody > a'
)
etc = soup.select(
    '.sub_read_list_box > dl > .etc '
)

data = []
for item in zip(title, link, content, etc):
    data.append(
        {
            'title' : item[0].text,
            'link' : item[1],
            'content' : item[2].text,
            'etc' : item[3].text
        }
    )

print(data)

driver.quit()