
# **Amazon Product Scraper**

This project is a Python-based web scraper that extracts product details such as **name**, **price**, and **ratings** from Amazon's search result pages. It uses **Selenium** for automated browser interaction and supports dynamic URL input. The scraper saves the scraped data into a CSV file for further analysis.

---

## **Features**

- Extracts **product name**, **price**, and **ratings** from Amazon product pages.
- Supports dynamic URL input for scraping different product categories or search results.
- Saves the scraped data into a CSV file with a unique filename based on the provided URL.
- Uses **Selenium WebDriver** for automated browsing and data extraction.
- Includes error handling for cases where data might be missing.
- Fully configurable via `requirements.txt` for dependency management.

---

## **Setup Instructions**

### **Prerequisites**

1. **Python 3.7+** installed on your system.
2. **Google Chrome** browser installed.
3. Matching version of **ChromeDriver** (already included in the project folder).

---

### **Install Dependencies**

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```

2. Install the required Python libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Usage**

1. Run the scraper script:
   ```bash
   python main.py
   ```

2. Enter the desired **Amazon URL** (e.g., `https://www.amazon.in/s?k=shoes`).

3. The script will:
   - Open the Amazon page in a Chrome browser.
   - Scrape product names, prices, and ratings.
   - Save the data into a CSV file named based on the provided URL (e.g., `shoes.csv`).

4. The generated CSV file will be saved in the project directory.

---

### **Example**

- **Input**:
  ```
  Enter the Amazon URL to scrape: https://www.amazon.in/s?k=shoes
  ```

- **Output**:
  A file named `shoes.csv` containing:
  | Product Name                   | Price  | Rating  |
  |--------------------------------|--------|---------|
  | Puma Men's Sneakers           | 1,999  | 4.3     |
  | Nike Air Max 270              | 9,499  | 4.5     |
  | ...                            | ...    | ...     |

---

## **Project Structure**

```plaintext
.
├── chromedriver.exe     # ChromeDriver for Selenium
├── main.py              # Main Python script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## **Important Notes**

- Ensure that the ChromeDriver version matches your installed **Google Chrome** version. If needed, download the correct version from [here](https://chromedriver.chromium.org/downloads).
- The scraper works best with Amazon's search result pages.
- For large-scale scraping, consider adding delays between requests to avoid being blocked by Amazon.

---

## **How to Contribute**

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a Pull Request on GitHub.

---

## **License**

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
