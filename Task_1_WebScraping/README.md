# CodeAlpha Web Scraping

## Project Overview

This project was developed as part of the CodeAlpha Data Analytics Internship.

The project demonstrates web scraping using Python and BeautifulSoup. Data is collected from a publicly available practice website and converted into a structured CSV dataset.

## Objective

The objective of this project is to:

- Extract data from a public website
- Understand and navigate HTML structure
- Collect information from multiple web pages
- Clean and structure the collected data
- Create a custom dataset in CSV format

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV
- VS Code

## Data Collected

The scraper collects:

- Book Title
- Price
- Rating
- Availability
- Product URL

## Scraping Process

Website
→ Send HTTP Request
→ Receive HTML
→ Parse HTML using BeautifulSoup
→ Extract book information
→ Clean the data
→ Create CSV dataset

## Dataset

The final dataset is stored in:

`books_dataset.csv`

The dataset contains the information collected from multiple pages of the practice website.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt