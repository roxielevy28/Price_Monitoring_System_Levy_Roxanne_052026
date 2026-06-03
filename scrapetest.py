import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com/catalogue/set-me-free_988/index.html')
soup = BeautifulSoup (page.content, 'html.parser')
print(soup)
product = soup.find(id="default")
print (product)

items = product.find_all(class_= 'container-fluid page')
print(items)

print(items[0].find(class_= 'product_pod').get_text())
print(items[0].find(class_= 'star-rating Five').get_text())

product_page_url = [items[0].find(class_= 'product_pod').get_text()]
review_rating = [items[0].find(class_= 'star-rating Five').get_text()]

print(product_page_url)
print(review_rating)
