from  urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')

namefindall = bs.find_all(text = 'the prince')
print(len(namefindall))

namefind = bs.find(text='the prince')
print(len(namefind))

title = bs.findAll( id = 'title' , class_ = 'text' )
for i in title:
    print(i)