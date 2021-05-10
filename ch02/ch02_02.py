from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, "html.parser")

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywaords) 
# find()와 findAll() 모두 거의 항상 처음 두 매개변수인 tag와 attributes만 사용하게 될 것임.
nameList=bs.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
print("-------------------------------------------------------------")

#How to deal with children and descendants
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")
for child in bs.find("table", {"id":"giftList"}).children:
    print(child)
print("-------------------------------------------------------------")

#How to deal with siblings
for sibling in bs.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)

print("-------------------------------------------------------------")

#How to deal with parents
print(bs.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())