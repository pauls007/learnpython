from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen ( 'http://www.pythonscraping.com/pages/page3.html' ) 
bs = BeautifulSoup ( html , 'html.parser')

''' 
1. สิ่งที่ต้องการหา คือ ราคา 15.00
2. เนื่องจากราคา 15.00 มันไม่มีชื่อ tag อะไรเลย
3. เข้าไปทำการหา tag img ก่อน 
4. ใช้ function: parent.previous_sibling ในการย้อนกลับมาเพื่อดึงข้อมูล
'''
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())