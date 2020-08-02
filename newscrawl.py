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

links = []
for link in soup.select('.sub_read_list_box > dl > .sbody> a'):
    if 'href' in link.attrs:
        conn = link.attrs['href']
        links.append(conn)
        
        
conn = soup.select('.sub_read_list_box > dl > .sbody > a')

# img = [] 
# for image in soup.select('.sub_read_list_box > .img_file > p > a > img '):
#     if 'src' in image.attrs:
#         img_src = image.attrs['src']
#         img.append(img_src)
# print(img)

content = soup.select(
    '.sub_read_list_box > dl > .sbody > a'
)
etc = soup.select(
    '.sub_read_list_box > dl > .etc '
)

data = []
kfdn = "http://www.kfdn.co.kr" # 식약일보 정책 링크, 기사별 href 만 변경 
for item in zip(title, links, content, etc):
    data.append(
        {
            'title' : item[0].text,
            'link' : kfdn+item[1],
            'content' : item[2].text,
            'etc' : item[3].text
        }
       )


print(data)