# pip install beautifulsoup4 requests

from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"

response = requests.get(url)

# print(response.status_code)
# print(response.headers)
#print(response.text)

# using bs4 to get response and parse it
soup = BeautifulSoup(response.text, "html.parser")
# quotes = soup.find_all("span", class_="text")
# #print(type(quotes))
# for quote in quotes:
#     print(quote.text)

authors = soup.find_all("small", class_="author")
for author in authors:
    print(author.text)