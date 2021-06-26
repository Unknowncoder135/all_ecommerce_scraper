from sys import version
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random   

from bs4 import SoupStrainer

main_list = []
serach_term = 'tv'
for item in range(1,7):
    url =f'https://www.ebay.com/sch/i.html?_nkw={serach_term}&_sop=12&_pgn={item}'
    print(url)
    headers = {'your.user agent'}
    r = requests.get(url,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    name = soup.find_all('h3',class_='s-item__title')
    img  = soup.find_all('img',class_='s-item__image-img')
    # print(img)
    prices = soup.find_all('span',class_='s-item__price')
    sold =soup.find_all('span',class_='BOLD NEGATIVE')

    where_is_from  = soup.find_all('span',class_='s-item__location s-item__itemLocation')
    seller = soup.find_all('span',class_='s-item__etrs-text')
    for z in range(0,len(name)):
        title = name[z].text
        try:
            price = prices[z].text
        except:
            price = 'None'
            
        try:
            imgs = img[z]['src']
        except:
             imgs = 'None'
        try:
            sold_prod = sold[z].text
         except:
        
            sold_prod = 'npne'
        try:
            location = where_is_from[z].text
        except:
            location = 'none'
         try:
            prod_seller = seller[z].text
        except:
             prod_seller = 'None'

        main_dir = {
            'prod_title':title,
            'prod_price':price,
            'prod_img_link':imgs,
            'prod_solding':sold_prod,
            'product_location':location,
            'prod_seller':prod_seller
        }
        main_list.append(main_dir)
    print(f'priting pag..{item}')
# print(main_list)
h = random.randrange(2,100)
data_frame = pd.DataFrame(main_list)

data_frame.to_csv(f'ebay_data{h}.csv',index=False)
print('mission_complate')
