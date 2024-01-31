# import requests
# from bs4 import BeautifulSoup

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get("https://www.zomato.com/bangalore/top-restaurants",headers=headers)

# content = response.content
# soup = BeautifulSoup(content,"html.parser")

# top_rest = soup.find_all("div")
# list_tr = top_rest[0].find_all("div",attrs={"class": "bke1zw-1 eMsYsc"})
# print(list_tr)


# import requests
# import bs4 as bs

# url = 'https://www.zomato.com/bangalore/top-restaurants'    
# req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})    
# html = req.text    
# soup = bs.BeautifulSoup(html, "html.parser")

# for item in soup.select('.search-result'):
# 	try:
# 		print('----------------------------------------')
# 		print(item)

# 	except Exception as e:
# 		#raise e
# 		print('Nill')

# ---------- USing Scrapy -------------- #


# import scrapy

# class Testicular(scrapy.Spider):
#     name = "Zomato Test"
#     start_urls = ["https://www.zomato.com/bangalore"]

#     def parase(self, response):

#         titles = response.xpath("//h2//text()").getall()

#         for title in titles:
#             print(title.strip())


from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# 1. Set up
PAT = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PAT)
url = "https://www.zomato.com/bangalore"
# 2. Access the website
driver.get(url)

# # Identify the container element (replace with actual selector)
# container = driver.find_element_by_css_selector('#root > div')
container = driver.find_element_by_xpath('//*[@id="root"]/div')
# print(container)
# while container.find_elements_by_xpath('//*[@id="root"]/div/div[9]'):
    
#     print(container.text)
    
    # nams = container.find_element_by_css_selector("#root > div > div:nth-child(10)")
    
    # print(nams)
# print(type(container))

# Extract restaurant names within the container
# restaurant_names = [
#     name.text for name in container.find_elements_by_xpath('/html/body/div[1]/div/div[11]')
# ]

# print(restaurant_names[0])
# Print the extracted names
# restaurant_names = restaurant_names.split("\n")
# for name in restaurant_names:
#     print(name)
# print(container.text)

# Starting pallet element
pallet_xpath_base = "/html/body/div[1]/div/div["

# Loop through pallets (adjust range as needed)
for i in range(10, 11):
    # Construct the current pallet XPath
    pallet_xpath = pallet_xpath_base + str(i) + "]"
    # print(type(pallet_xpath))

    # Find the current pallet element
    pallet_element = container.find_elements_by_xpath(pallet_xpath)
    print(pallet_element.text)

    
    # for pallet_element in container.find_elements_by_xpath(pallet_xpath):  # Iterate through list
    #     print(pallet_element.get_attribute())
    #     restaurant_names = [
    #         name.text
    #         for name in pallet_element.find_elements_by_xpath('')
    #     ]
        # print(restaurant_names)
        # restaurant_prices = [
        #     price.text for price in pallet_element.find_elements_by_xpath("/html/body/div[1]/div/div[92]/div/div[1]/div/div/a[2]/div[2]/p[2]")
        # ]

    # Print the extracted information
    # print(f"\nPallet {i}:")
    # for name, price in zip(restaurant_names, restaurant_prices):
    #     print(f"- {name}: {price}")

# driver.quit()

# # '/html/body/div[1]/div/div[10]/div/div[1]/div/div/a[2]/div[1]/h4'