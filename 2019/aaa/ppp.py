import requests
from bs4 import BeautifulSoup

h = {'Referer': 'http://siping.bitauto.com/?referrer=https://www.baidu.com/link?url=yn8SckE9YN_PmqmrNkM-uygt9uXkFdRleKOeZ__B5ZG-dpaSE76pqHRGLDDiynnu&wd=&eqid=e009a16d00215973000000035da027e9'
    'Host':'car.bitauto.com'
    }

r = requests.get('http://car.bitauto.com/jincouxingche/',headers=h)

c = r.text

soup = BeautifulSoup(c,'html.parser')

contents = soup.find('div',{'class':'row blok-4col-180'})
print(contents)


