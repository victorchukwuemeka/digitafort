#from pydoc import text
import requests;
from bs4 import BeautifulSoup;


url = "https://quotes.toscrape.com"
print(f"fetching {url}")

response = requests.get(url)
print(f"response code {response.status_code}")
if response.status_code != 200:
    print(f"failed response code {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:500])

quotes  = soup.find_all("div", class_="quotes")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print(f"{text} - {author}")
    