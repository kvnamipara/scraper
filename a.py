import requests

page= requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print page.status_code