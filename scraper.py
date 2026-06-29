from bs4 import BeautifulSoup
import requests
import os 
for i in range(1,19):
    page_to_scrape=requests.get(f"https://vedabase.io/en/library/bg/{i}/")
    soup=BeautifulSoup(page_to_scrape.text,"html.parser")
    quotes=soup.findAll("span")
    #authors=soup.findAll("small",attrs={"class":"author"})
    with open("tst.txt","a",encoding="utf-8") as f:
        for quote in quotes:
            text=quote.get_text(strip=True)
            if text.startswith("Thanks") or "Saurabh" in text:
                continue
            if text in ["Bhaktivedanta", "™", "Settings", "English", "en", "View"]:
                continue
            print(quote.text + '\n')
            f.write(quote.text + '\n')
