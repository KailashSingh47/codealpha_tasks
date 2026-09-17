import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

BASE_URL = "https://books.toscrape.com/"

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

data = []

# Scrape first 5 pages
for page in range(1, 6):

    if page == 1:
        url = BASE_URL
    else:
        url = urljoin(
            BASE_URL,
            f"catalogue/page-{page}.html"
        )

    print(f"Scraping page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    for book in books:

        title = book.h3.a["title"]

        price_text = book.find(
            "p",
            class_="price_color"
        ).text.strip()

        price = float(
            price_text.replace("£", "")
            .replace("Â", "")
            .strip()
        )

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating_element = book.find(
            "p",
            class_="star-rating"
        )

        rating_name = rating_element["class"][1]
        rating = rating_map[rating_name]

        relative_url = book.h3.a["href"]

        product_url = urljoin(
            url,
            relative_url
        )

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })


# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv(
    "books_dataset.csv",
    index=False
)

print("\n" + "=" * 50)
print("SCRAPING COMPLETED")
print("=" * 50)

print("Total books collected:", len(df))
print("Dataset saved as: books_dataset.csv")

print("\nFirst 5 records:")
print(df.head())