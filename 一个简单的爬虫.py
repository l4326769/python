import requests as r
from bs4 import BeautifulSoup
lis=list()
ad=r.get('****')
soup=BeautifulSoup(ad.text,'html.parser')

lili=soup.find_all('div',class_="******")
soups=BeautifulSoup(lili.__str__(),'html.parser')
lili=soups.find_all('img')
for y in lili:
    lis.append(y.get('src'))
print(lis)