## Craigslist Price Retriever & Title
## Beginning practice with getting values from websites
import requests
from bs4 import BeautifulSoup

## gets the url information and saves it as the variable r
##works with specific craigslist postings.
url = "https://knoxville.craigslist.org/reo/d/x80-mobile-home/6505412177.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

##finds price and title text and prints those values from website
price_data = soup.find("span", {"class": "price"})
title_data = soup.find("span", {"id": "titletextonly"})
print("price is " + price_data.text)
print("Title: " + title_data.text)
