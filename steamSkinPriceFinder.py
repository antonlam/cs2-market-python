import requests
from bs4 import BeautifulSoup
import webbrowser
import os

def createUrl(webCode, num):
    f = open(f"Url_{num}.html","w", encoding='utf-8-sig')
    f.write(webCode)
    f.close()
    

def steamFindFilterItem(steamurl):
    urls=[]
    r = requests.get(steamurl)
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all(class_="market_listing_row_link")
    hrefs = [link["href"] for link in links]

    for href in hrefs:
        urls.append(href)
        
    return urls

if __name__ == "__main__":
    
    print("Please enter an address of an item:")
    print("e.g. StatTrak™ Glock-18 Oxide Blaze:\nhttps://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20Glock-18%20%7C%20Oxide%20Blaze%20%28Field-Tested%29")
    url = input("URL: ")

    r = requests.get(url)
    if(r.status_code == 200):
        soup = BeautifulSoup(r.text, "html.parser")

        pricesWithFee =  soup.find_all(class_='market_listing_price market_listing_price_with_fee')
        pricesWithoutFee = soup.find_all(class_='market_listing_price market_listing_price_without_fee')
        for i in range(len(pricesWithoutFee)-1):
            print(f"Item {i+1}")
            print("Price with fee:" + pricesWithFee[i].get_text(strip=True))
            print("Price without fee:" +pricesWithoutFee[i].get_text(strip=True))
    else:
        print("URL not found")
