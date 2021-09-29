import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "YOUR EMAIL"
PASSWORD = "PASSWORD"

amazon_url = "AMAZON PRODUCT URL"
flipkart_url = "FLIPKART PRODUCT URL"

fresponse = requests.get(flipkart_url)
product_page = fresponse.text

fsoup = BeautifulSoup(product_page, "lxml")
famount = fsoup.find(name="div", class_="_30jeq3 _16Jk6d").get_text()

fprice_split = famount.split("₹")[1]
fvalue1 = fprice_split.split(",")[0]
fvalue2 = fprice_split.split(",")[1]
flipkart_final_price = int(fvalue1 + fvalue2)
print(flipkart_final_price)


amazon_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Cookie": "PHPSESSID=ajf5mjhe6tfiv9jn71h3i9pc31; _ga=GA1.2.1512257273.1632120106; _gid=GA1.2.1507113444.1632120106"
}

response = requests.get(amazon_url, headers=amazon_headers)
product_page = response.text

soup = BeautifulSoup(product_page, "lxml")
current_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_split = current_price.split("₹")[1]
val = price_split.split(".")[0]
value1 = val.split(",")[0]
value2 = val.split(",")[1]
amazon_final_price = int(value1 + value2)
print(amazon_final_price)


if amazon_final_price < flipkart_final_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Low price alert!!!!."
                f"\n\nThe product which you are searching is cheaper on AMAZON click on this link to buy: {amazon_url}"
            )

else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Low price alert!!!!."
                f"\n\nThe product which you are searching is cheaper on FLIPKART click on this link to buy: {flipkart_url}"
            )
