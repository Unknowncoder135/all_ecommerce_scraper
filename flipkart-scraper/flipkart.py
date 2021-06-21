from sys import version
from bs4 import BeautifulSoup
import requests
from bs4 import SoupStrainer
import pandas as pd
from requests.api import options
import random


main_list = []
search_term = 'vivo'

for z in range(1,10):
    url =f'https://www.flipkart.com/search?q={search_term}&page={z}'
    r = requests.get(url)
    soup  = BeautifulSoup(r.text,'html.parser')
    title = soup.find_all('div',class_='_4rR01T')
    # print(title)
    price = soup.find_all('div',class_='_30jeq3 _1_WHN1')
    imgs = soup.find_all('img',class_='_396cs4 _3exPp9')
    rateings = soup.find_all('div',class_='_3LWZlK')
    discrept = soup.find_all('ul',class_='_1xgFaf')

    for x in range(0,len(title)):
        titles = title[x].text
        prices  =price[x].text.replace('₹','')
        try:
            img = imgs[x]['src']
            rateing  = rateings[x].text
            discription = discrept[x].text
        except:
            img = 'not found'
            rateing = 'not found'
            discription = 'not found'
        main_dir = {
            'product_name':titles,
            'product_price': prices,
            'product_img_link': img,
            'product_rateing': rateing,
            'product_discription': discription
        }
        main_list.append(main_dir)
    print(f'scrping page{z}...')


h = random.randrange(2,100)
dataframe = pd.DataFrame(main_list)
dataframe.to_csv(f'flipkart{h}.csv',index=False,header=False)

