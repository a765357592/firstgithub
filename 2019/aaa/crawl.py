import requests
from bs4 import BeautifulSoup


r = requests.get('https://xiaoshuo.sogou.com/29_0_0_0_heat/')

c = r.content

soup = BeautifulSoup(c,'html.parser')


f = soup.find('ul',{'class':'filter-ret clear'})
items = f.find_all('li',{'class':'fl clear'})
for (i,item) in enumerate(items):
    title = item.find('h3').find('a').text
    intro = item.find('div',{'class':'d2'}).text
    img = item.find('img')['src']
    print(i,title,'\t',intro,img)
