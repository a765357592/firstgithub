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
    pageJob = []
    for job in j_content:
        jobDic = {}

        pageJob.append(jobDic)
    return pageJob

pool = mp.Pool()
multi_res = [pool.apply_async(crawl_page,(url,))for url in urls]
pageJobs = [res.get() for res in multi_res]

for pageJob in pageJobs:
    for job in pageJob:
        jobs.append(job)

print(len(jobs))
t2 = time.time()
print(t2-t1)