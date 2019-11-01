
import bbb

import requests
from bs4 import BeautifulSoup
import multiprocessing as mp 
import time

t1 = time.time()
r = requests.get('https://bj.1010jz.com')
c = r.text
soup = BeautifulSoup(c,'html.parser')

contents = soup.find('div',{'class':'PartTimea'})
jobs = []

urls = ['https://bj.1010jz.com']
print(contents)

def crawl_page(url):
    j_r = requests.get(url)
    j_c = j_r.text
    j_soup = BeautifulSoup(j_c,'html.parser')
    j_content = j_soup.find_all('div',{'class':'PartTimea'})
    return j_content


pool = mp.Pool()
multi_res = [pool.apply_async(crawl_page(urls))]

print(multi_res)
t2 = time.time()
print(t2-t1)

bbb.create_db()
for job in jobs:
    bbb.insert_car(job['name'])
sql=bbb.view_all()
print(sql)