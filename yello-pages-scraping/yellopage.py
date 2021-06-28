import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

main_list = []

def get_data(url):
    headers = {'User-Agent': 'put your user agent'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('div', class_ = 'row businessCapsule--mainRow')

def parse(articles):
    for item in articles:
        name = item.find('h2',{'itemprop': 'name'}).text.strip()

        address = item.find('span', {'itemprop': 'address'}).text.strip().replace('\n', '')
        try:
            rateings = item.find('span',class_='starRating--average').text
        except:
            rateings = 'none'
        try:
            website = item.find('a', class_ = 'btn btn-yellow businessCapsule--ctaItem')['href']
        except:
            website = ''
        try:
            tel = item.find('span', class_ = 'business--telephoneNumber').text.strip()
        except:
            tel = ''
    
        all_info = {
            'name': name,
            'address': address,
            'website': website,
            'tel': tel,
            'rateings': rateings,
            
        }
        main_list.append(all_info)
    return

def load_data():
    df = pd.DataFrame(main_list)
    h = random.randrange(0,150)
    df.to_csv(f'mrdon{h}.csv', index=False)

for x in range(1,9):
    print(f'Getting data page..... {x}')
    articles = get_data(f'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=540269558&keywords=cafes+%26+coffee+shops&location=glasgow&pageNum={x}')
    parse(articles)
    time.sleep(3)

load_data()
print('mission Complate')
