


# shopify scrping
# helemboost.com
from sys import version
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from bs4 import SoupStrainer
url ='https://helmboots.com/products.json?limit=500&page=1'
r = requests.get(url)
data  = r.json()
# print(data['products'][0]['title'])
main_list=[]
# FATCHING PROCESS
for x in data['products']:
    # print(x['title'])
    title = x['title']
    handle = x['handle']
    create = x['created_at']
    update = x['updated_at']
    vendor = x['vendor']
  
    for z in x['images']:
      
        try:
            img = z['src']
        except:
            img = 'None'
    for w in x['variants']:
        sku = w['sku']
        tit  = w['title']
        price = w['price']
        available = w['available']

# STORE IN DIRECTORY
        main_product ={
            'title':title,
            'handle':handle,
            'create_date':create,
            'update_date': update,
            'vendor':vendor,
            'sku':sku,
            'tit':tit,
            'price':price,
            'available':available,
            'img_src_link':img
        }
        main_list.append(main_product)

        # print(available,tit,sku,price)
    
# print(main_list)
# STORE IN CSV FILE PROCESS START BELOW
csv_file = pd.DataFrame(main_list)
csv_file.to_csv('product_data.csv',index=False)
print('process_ complate')

