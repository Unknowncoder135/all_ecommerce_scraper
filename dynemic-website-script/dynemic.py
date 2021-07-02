from sys import version
from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4 import SoupStrainer
main_list = []

url ='https://www.thewhiskyexchange.com'
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
main_url = 'https://www.thewhiskyexchange.com/c/33/american-whiskey'
r = requests.get(main_url,headers=headers)
soup  = BeautifulSoup(r.text,'lxml')

nam = soup.find_all('li',class_='product-grid__item')
print(len(nam))
list = []
for x in nam:
    for link in x.find_all('a',href=True):
        # print(link['href'])
        list.append(url + link['href'])




test = 'https://www.thewhiskyexchange.com/p/60915/wilderness-trail-settlers-select-rye-british-bourbon-society-pick'

for mm in list:
    r = requests.get(mm,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    # for x in 
    name = soup.find('h1',class_='product-main__name').text.replace('\n','')
    price = soup.find('p',class_='product-action__price').text.replace('\n','')
    leter_ml = soup.find('p',class_='product-main__data').text.replace('\n','')
    # print(name)
    main_dir  = {
        'name_':name,
        'price':price,
        'ml_or_leter': leter_ml
    }
    main_list.append(main_dir)
print(main_list)
# print(main_dir)


dfs  = pd.DataFrame(main_list)
dfs.to_csv('data.csv',index=False)