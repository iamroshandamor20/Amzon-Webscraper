from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
import os
from datetime import datetime

# Function to scrape Amazon products
def scrape_amazon_products(url):
    # Chrome driver setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_service = Service("chromedriver.exe")  # Path to chromedriver.exe

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)

    # Let the page load completely
    time.sleep(5)

    # Lists to store data
    product_names = []
    product_prices = []
    product_ratings = []

    try:
        # Find product names
        name_elements = driver.find_elements(By.CLASS_NAME, "a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2")
        product_names = [name.text for name in name_elements]

        # Find product prices
        price_elements = driver.find_elements(By.CLASS_NAME, "a-price-whole")
        product_prices = [price.text for price in price_elements]

        # Find product ratings using the aria-label attribute
        rating_elements = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'out of 5 stars')]")
        product_ratings = [rating.get_attribute("aria-label").split(' ')[0] for rating in rating_elements]

        # Combine data
        products = []
        for i in range(len(product_names)):
            product = {
                "Name": product_names[i] if i < len(product_names) else "N/A",
                "Price": product_prices[i] if i < len(product_prices) else "N/A",
                "Rating": product_ratings[i] if i < len(product_ratings) else "N/A",
            }
            products.append(product)

        # Save to CSV
        save_to_csv(products)

    except Exception as e:
        print(f"Error while scraping: {e}")

    finally:
        driver.quit()

# Function to save data to a CSV file
def save_to_csv(data):
    # Create a filename based on the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"amazon_products_{current_time}.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Price", "Rating"])
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error while saving to CSV: {e}")

# Main function to prompt the user for a URL
if __name__ == "__main__":
    url = input("Enter the Amazon URL to scrape: ").strip()
    if url:
        scrape_amazon_products(url)
    else:
        print("Invalid URL!")
