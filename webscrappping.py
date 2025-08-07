from bs4 import BeautifulSoup
import requests
import csv 
url="https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7VK2X/ref=sr_1_4?crid=3HARED7C3TW8Y&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGl59wye_6IA_t9o-39YExbo3TVSRWk2cjW_Vt4hOATlJ7fdsMx5F1sinpbUPXEMDsB4ruKjZ40i6qSq6kAGfuB-aS3M5nn7vphQvhmLyQLltrYD36YibrahJyO_cvqWvVpprT2_wcl5XLDE-1VtKp_oCLKpaYbfbhKeopNEg5GXqfSDiM9fZx_WHMQYwInVLQjdZToaJMlS1pCZx7bzVKa9s.u7BpM4pPiN4Ppj8zeQRhOVwygdrWT24eN1lFKz4gWeA&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1754399213&sprefix=%2Caps%2C211&sr=8-4&th=1"
headers={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.3https://www.amazon.in/Sonos-Ace-Wireless-Headphones-Cancellation/dp/B0D37R7X6Z/ref=sr_1_2_sspa?crid=3HARED7C3TW8Y&dib=eyJ2IjoiMSJ9.y06"}

response=requests.get(url,headers=headers)

if response.status_code==200:
    print("success",response.status_code)
    html_content=response.text
else:
    print("fetching error",response.status_code)

soup=BeautifulSoup(html_content,'lxml')
#print(soup.prettify())
product_title=soup.find("span",id="productTitle").text.strip()
if product_title:
    print("Product Title:",product_title) 
else:
    print("Product Title is not available")
print()
product_price=soup.find("span",class_="a-price-whole").text.strip()
if product_price:
    print("Product Price:",product_price) 
else:
    print("Product Price is not available")
print()
product_rating=soup.find("span",id="acrPopover").text.strip()
if product_rating:
    print("Product Rating:",product_rating) 
else:
    print("Product Rating is not available")
print()
product_bulletpoint=soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
if product_bulletpoint:
    print("Product Bulletpoint:",product_bulletpoint) 
else:
    print("Product Bulletpoint is not available")
print()
product_description=soup.find("div",id="productDescription").text.strip()
if product_description:
    print("Product Description :",product_title) 
else:
    print("Product Description is not available")
print()
product_reviews=soup.find("ul",id="cm-cr-dp-review-list").text.strip()
if product_reviews:
    print("Product Review:",product_reviews) 
else:
    print("Product Review is not available")
#saving the file data
with open("amazon_airpod pro max.csv",mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["product_title","product_price","product_rating","product_bulletpoints","product_description","product_reviews"])
    writer.writerow([product_title,product_price,product_rating,product_bulletpoint,product_description,product_reviews])

print("data has been saved successfully in csv file")
