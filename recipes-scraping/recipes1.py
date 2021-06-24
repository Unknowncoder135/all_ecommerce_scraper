from sys import version
from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4 import SoupStrainer

main_list = []
main=[]
for k in range(1,10):

    url =f'https://www.allrecipes.com/recipes/17567/ingredients/?page={k}'
    r = requests.get(url)
    soup  = BeautifulSoup(r.text,'html.parser')

    name = soup.find_all('span',class_='tout_titleLinkText')
    no = soup.find_all('noscript')
    review = soup.find_all('span',class_='card__ratingCount card__metaDetailText')

    for z in no:
        f = z.find('img')['src']
       
        main.append(f)

    for item in range(0,len(name)):
        title = name[item].text.strip()
        # ff = item.find()
        reviews = review[item].text.strip()
        # print(title)
        mai_dir = {
            'title': title,
            'img_link':main[item],
            'review': reviews

        }
        main_list.append(mai_dir)
    print(f'printing page.....{k}')
print(main_list)

data = pd.DataFrame(main_list)
data.to_csv('data2.csv',index=False)
print('complate')
