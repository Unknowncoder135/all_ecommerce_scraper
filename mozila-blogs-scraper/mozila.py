from sys import version
from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4 import SoupStrainer


main_list = []

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    return soup
# print(r.status_code)
# print(soup.title)
def parse(soup):
    main = soup.find('div',class_="ft-c-post-list__wrap--three-column")

    seeson  = main.find_all('section',class_="mzp-c-card mzp-has-aspect-1-1")

    for x in seeson:
        title = x.find('h2',class_="mzp-c-card-title").text
        tag = x.find('div',class_='ft-c-pill').text
        # dd = x.find('div',class_="mzp-c-card-image wp-post-image")
        try:
            img_link = x.find('img',class_="mzp-c-card-image wp-post-image")['src']
        except:
            img_link = 'none'
        main_dir = {
            'title':title,
            'tag_name':tag,
            'img_link':img_link
        }
        main_list.append(main_dir)
    # print(img_link)
# print(main)

def load(main_list):
    df = pd.DataFrame(main_list)
    df.to_csv('maindata.csv',index=False)


m = 1


while(m<20):
    url =f"https://blog.mozilla.org/en/category/mozilla/page/{m}/"
    print(url)
    print(f'page..{m}')
    soup = get_data(url)
    parse(soup)
    m=m+1
load(main_list)