import requests
import lxml
import fake_useragent
from bs4 import BeautifulSoup

url = 'https://kups.club/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('div', class_ ='col-lg-4 col-md-4 col-sm-6 portfolio-item')

for product in products:

    title_product = product.find('h3', class_ = 'card-title')
    price_product = product.find('p', class_ = 'card-text')
    shop_product = product.find('a', class_ = 'text-black link-default')

    print(title_product.text, price_product.text, shop_product.text)



