import requests
from bs4 import BeautifulSoup


r = requests.get('https://car.autohome.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html')

c = r.content

soup = BeautifulSoup(c,'html.parser')

content = soup.find_all('div',{'class':'tlist-cont'})

print(content)

