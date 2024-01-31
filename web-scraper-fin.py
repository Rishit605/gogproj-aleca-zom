# ----------- USING BEAUTIFULSOUP4 ----------------------- #

# import requests
# import bs4 as bs

# url = 'https://www.zomato.com/bangalore/restaurants'    
# req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})    
# html = req.text
# soup = bs.BeautifulSoup(html, "html.parser")
# print(soup.find_all("div", {'class':"sc-1mo3ldo-0 sc-gcJTYu letkfm"}))
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

# ------------------------- #

from selenium import webdriver
from selenium.webdriver.common.by import By

# PAT = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
url = "https://www.zomato.com/bangalore"

driver.get(url)


container = driver.find_element(By.XPATH, '//*[@id="root"]/div')

# container2 = container.find_element(By.XPATH,'//*[@id="root"]/div/div[9]')
# print(driver)

# Starting pallet element
pallet_xpath_base = "/html/body/div[1]/div/div["


# Loop through pallets (adjust range as needed)
for i in range(10, 21):
    # Construct the current pallet XPath
    pallet_xpath = pallet_xpath_base + str(i) + "]"
    # print(pallet_xpath)
    
    # Find the current pallet element
    pallet_element = container.find_elements(By.XPATH, pallet_xpath)
    # pallet_elements = container.find_element(By.XPATH, pallet_xpath)

    # print(pallet_elements.find_element(By.XPATH, '/html/body/div[1]/div/div[10]/div/div[1]/div/div/a[2]'))
    
    CARD_PATH = "/html/body/div[1]/div/div[10]/div/div["

    for pallet_element in container.find_elements(By.XPATH, pallet_xpath):  # Iterate through list
        print(pallet_element)

        # for i1 in range(1, 3):
        #     card_xpath = CARD_PATH + str(i1) + "]"
        #     print(pallet_element.find_elements(By.XPATH, card_xpath))

        
    # Implicit wait inside the loop (not recommended for frequent use)
    # driver.implicitly_wait(5)
driver.close()