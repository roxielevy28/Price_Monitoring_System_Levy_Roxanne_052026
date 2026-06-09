from urllib.parse import urljoin
import pandas as pd 
import request
from bs4 import BeautifulSoup

catergory= requests.get('https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html')
soup = BeautifulSoup (page.content, 'html.parser')

books_on_page= product.find_all(class_= 'product_pod')

raw_link=(books_on_page[0].find('h3').find('a')['href'])
Actual_link= urljoin("https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html", raw_link)
print(Actual_link)
