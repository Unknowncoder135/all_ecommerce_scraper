from sys import version
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import json
from bs4 import SoupStrainer


main_list= []
serach_term  = 'vivo'
for x in range(1,6):
    url =f'https://www.costco.com/televisions.html?currentPage={x}'
    headers = {'User-Agent': 'put your user agent '}
    r = requests.get(url, headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    main  = soup.find('div',class_='product-list grid')
    main_div = main.find_all('div',class_='col-xs-6 col-lg-4 col-xl-3 product')


    for c in main_div:
        price = c.find('div',class_='price').text.strip()
        name = c.find('span',class_='description').text.strip()
        try:
            img = c.find('img',class_='img-responsive')['src']
        except:
            img = 'none'
        try:
            rateing = c.find('span',class_='offscreen').text.strip()
        except:
            rateing = 'none'
        main_dir = {
            'produt_name':name,
            'produt_price':price,
            'produt_img':img,
            'produt_rating':rateing
        }
        main_list.append(main_dir)
        print(main_dir)
    print(f'page{x}')



df = pd.DataFrame(main_list)
df.to_csv('dataa.csv',index=False)
print('mission complate')
 
