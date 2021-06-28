import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

main_list = []

def extract(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find_all('div', class_ = 'row businessCapsule--mainRow')

def transform(articles):
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
    articles = extract(f'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=540269558&keywords=cafes+%26+coffee+shops&location=glasgow&pageNum={x}')
    transform(articles)
    time.sleep(5)

load_data()
print('mission Complate')