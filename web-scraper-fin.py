# ----------- USING BEAUTIFULSOUP4 ----------------------- #

import requests
import bs4 as bs

url = 'https://www.zomato.com/bangalore/restaurants'    
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})    
html = req.text
soup = bs.BeautifulSoup(html, "html.parser")
print(soup.find_all("div", {'class':"sc-1mo3ldo-0 sc-gcJTYu letkfm"}))
# print(soup)

# for link in soup.find_all('a'):
#     print(link.get('href'))
# list_items = soup.select('h4')
# print(list_items)
# for item in list_items:
#     print(item)
# for item in soup.select('h4'):
#     try:
#         # print('----------------------------------------')
#         print(item)
#         # print(item.select('.result-title')[0].get_text())
#     except Exception as e:
# 		#raise e
#         print('Nill')



# from bs4 import BeautifulSoup
# import requests

# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
# url = 'https://www.zomato.com/ncr/restaurants/pizza'

# response=requests.get(url,headers=headers)

# soup=BeautifulSoup(response.content,'lxml')

# #print(soup.select('[data-lid]'))
# for item in soup.select('.search-result'):
# 	try:
# 		print('----------------------------------------')
# 		#print(item)

# 		print(item.select('.result-title')[0].get_text())

# 	except Exception as e:
# 		#raise e
# 		print('')