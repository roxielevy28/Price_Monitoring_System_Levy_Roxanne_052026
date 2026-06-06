import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com/catalogue/set-me-free_988/index.html')
soup = BeautifulSoup (page.content, 'html.parser')
# print(soup)

product = soup.find(id="default")
# print(product)

items = product.find_all(class_= 'col-sm-6 product_main')
# print(items)

Book_Title=(items[0].find('h1').get_text())
# print(Book_Title)

quantity_available=(items[0].find(class_= 'instock availability').get_text())
# print(quantity_available)

Book_rating=items[0].find(class_='star-rating')['class'][1]
rates={"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5"}
review_rating= rates[book_rating]
# print(review_rating)

items_1[0] = product.find(class_= 'carousel')
Image_URL=(items_1[0].find('img') ['src'])
print(Image_URL)

items_2[0] = product.find_all(class_= 'table table-striped')

# ⚠️ SYNTAX: `items[2]` should probably be `items_2[0]` — check your variable names.
#   Also, the `find(class_= '')` has an empty class name. What class or tag are you
#   actually looking for inside the table?
print(items[2].find(class_= '')

# ⚠️ SYNTAX: Variable names cannot contain spaces. Also, `find_` is incomplete —
#   `find()` needs arguments. You need to figure out *which* `<td>` contains each
#   piece of data. Think about using the `<th>` text (like "UPC", "Price (excl. tax)")
#   to locate the right row, then grab the `<td>` next to it.
universal_ product_code (upc) = items_2[0].find_
price_including_tax = items_2[0].find_
price_excluding_tax

print(quantity_available)
print(review_rating)

# ⚠️ SYNTAX: `pd` is not imported. You need `import pandas as pd` at the top.
# ⚠️ SYNTAX: A DataFrame needs a dictionary with *key: value* pairs, not just a
#   set of strings. Example: {"column_name": [value1, value2]}
# ❓ HINT: You still need to extract these fields from the page:
#   - book_title: look inside the `<h1>` in `product_main`
#   - product_description: look for the `<div>` with id="product_description",
#     then get the text from the `<p>` tag that follows it
#   - category: look at the breadcrumb `<ul class="breadcrumb">` — which `<a>`
#     link is the category (not "Home" or "Books")?
#   - image_url: look for the `<img>` tag inside `<div class="item active">`
#   - product_page_url: this is just the URL you used in requests.get()

product_page_url = ('https://books.toscrape.com/catalogue/set-me-free_988/index.html')
# print(product_page_url)

Book_Report = pd.DataFrame(
    {
    "product_page_url",
    "universal_product_code",
    "book_title",
    "price_including_tax",
    "price_excluding_tax",
    "quantity_available",
    "product_description",
    "category",
    "review_rating",
    "image_url"
    })
    print(Book_Report)