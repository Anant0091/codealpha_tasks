# Task 1: Web Scraping

**Project:** Books website se data scrape karna

**Description:**  
Books.toScrape website se book title, price aur rating scrape kiya using Python.

**Technologies Used:**  
- Requests  
- BeautifulSoup  
- Pandas

**Files:**
- `web_scraping.py`
- `scraped_books.csv`
  # Task1_WebScraping/web_scraping.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text

        books.append({
            "Title": title,
            "Price": price
        })

    df = pd.DataFrame(books)
    df.to_csv("scraped_books.csv", index=False)

    print(f"Scraping completed successfully!")
    print(f"Total books scraped: {len(df)}")

except requests.exceptions.RequestException as e:
    print("Error while fetching website:", e)
