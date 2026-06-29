from urllib.parse import urljoin
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

def scrape_one_book(url):
    page = requests.get(url)
    soup = BeautifulSoup (page.content, 'html.parser')

    product = soup.find(id="default")
    items = product.find_all(class_= 'col-sm-6 product_main')

    book_title=(items[0].find('h1').get_text())

    raw_quantity = items[0].find(class_='instock availability').text.strip()
    quantity_available = int(re.search(r'\d+', raw_quantity).group())

    book_rating=items[0].find(class_='star-rating')['class'][1]
    rates={"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5"}
    review_rating= rates[book_rating]

    carousel = product.find(class_= 'carousel')
    image=(carousel.find('img') ['src'])
    image_url= urljoin(url, image)

    items[0] = product.find(class_= 'breadcrumb')
    category=items[0].find_all('a')[2].text.strip()

    description_block = product.select_one('#product_description + p')
    product_description = description_block.get_text(' ', strip=True) if description_block else ''

    info_table = product.find('table', class_='table-striped')
    table_data = {}
    for row in info_table.find_all('tr'):
        header = row.find('th').text.strip()
        value = row.find('td').text.strip()
        table_data[header] = value

    universal_product_code = table_data.get ('UPC')
    price_including_tax = table_data.get ('Price (incl. tax)')
    price_excluding_tax = table_data.get ('Price (excl. tax)')
   
    product_page_url = url

    return {
            'product_page_url': product_page_url,
            'universal_product_code': universal_product_code,
            'book_title': book_title,
            'price_including_tax': price_including_tax,
            'price_excluding_tax': price_excluding_tax,
            'quantity_available': quantity_available,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url,
    }
