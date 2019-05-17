import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests

headers_std = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Content-Type': 'text/html',
}

asins_df = pd.read_csv('ASINs.csv')
# print(asins_df.head())

asin_list = asins_df['ASIN']
# print(asin_list)

# for asin in asin_list:
# 	url = "https://www.amazon.in/dp/" + str(asin)
# 	html = requests.get(url,headers=headers_std).text
# 	soup = BeautifulSoup(html,'lxml')

# url = "https://www.amazon.in/dp/B014G69R1Q"
# html = requests.get(url,headers=headers_std).text
# soup = BeautifulSoup(html,'lxml')

image_list_span_class = 'a-button-text' #span containing the img tag
brand_name_class = 'bylineInfo'  #can get link of brand and name of brand from the a-link
product_name_class = 'productTitle' #span
rating_class = 'a-icon-alt'  #span
no_of_rat_class = 'acrCustomerReviewText' #span
actual_price_class = 'priceBlockStrikePriceString'
sell_price_id = 'priceblock_saleprice'

#scrape the product details
image_list = soup.find_all('span',{'class':image_list_span_class})
brand_name = soup.find_all('a',{'id':brand_name_class})
product_name = soup.find_all('span',{'id':product_name_class})
rating = soup.find_all('span',{'class':rating_class})
no_of_rat = soup.find_all('span',{'id':no_of_rat_class})
actual_price = soup.find_all('span',{'class':actual_price_class})
selling_price = soup.find_all('span',{'id':sell_price_id})

image_urls = []

for image in image_list:
	try:
		image_url = image.find('img').get('src')
		print(image_url)
		image_urls.append(image_url)
	except:
		# print('NoneType Object in soup')
		pass

print(brand_name[0].text.strip())
print(product_name[0].text.strip())
print(rating[0].text.strip())
print(no_of_rat[0].text.strip())
print(actual_price[0].text.strip())
print(selling_price[0].text.strip())