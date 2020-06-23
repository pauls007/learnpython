from  urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')

nameList = bs.find_all('span',{'class':'green'})
a = bs.findAll('span',{'class':'green'})

print("มีการใช้ .get_text(): ")
for name in nameList:
    print(name.get_text())

print("=============================================================")

print("ไม่มีการใช้ .get_text():  ")
for name in nameList:
    print(name)

print("=============================================================")

print("ไม่มีการใช้อะไรเลย มีแต่ findAll:  ")
for x in a:
    print(x)

print("=============================================================")