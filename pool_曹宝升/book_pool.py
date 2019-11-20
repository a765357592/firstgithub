import requests
from bs4 import BeautifulSoup
import multiprocessing as mp 
import time

t1= time.time()

def getbooks():
    r = requests.get('https://www.17k.com/all/book/2_22_126_0_0_0_0_0_1.html')
    c = r.text
    soup = BeautifulSoup(c,'html.parser')
    page_div = soup.find('div',{'class':'main searchjg'})
    a1 = page_div.find('div',{'class':'search-list'}).find('div',{'class':'alltable'})
    urls = ['https://www.17k.com/all/book/2_22_126_0_0_0_0_0_'+str(i)+'.html' for i in range(1,8)]
    page_r = requests.get(urls)
    page_c = page_r.text
    soup_1 = BeautifulSoup(page_c,'html.parser')
    page_div1 = soup_1.find('div',{'class':'main searchjg'})
    a2 = page_div1.find('div',{'class':'search-list'}).find('div',{'class':'alltable'})
    a3 = a2.find('table').find('tbody')
    a4 = a3.find_all('tr',{'class':'bg0'})
    books = []
    for book in a4:
        a_book = {}
        a_book['number']=book.find('td',{'class':'td1'}).text
        a_book['name']=book.find('td',{'class':'td3'}).text
        a_book['author']=book.find('td',{'class':'td6'}).text
        books.append(a_book)
    return books