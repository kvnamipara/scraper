import requests
from bs4 import BeautifulSoup

page= requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content,'html.parser')
#print soup.prettify()
a=list(soup.children)

#print [type(item) for item in a]

html= a[2]
#print html
html_children = list(html.children)
#print html_children
body = html_children[3]
#print list(body.children)
p= list(body.children)[1]
#print p.get_text()


##finding all intance at once
print soup.find_all('p')

##only first instance
print soup.find('p')