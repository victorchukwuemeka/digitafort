# Complete Python Web Scraping Course

## Module 1: Foundations & Setup

### 1.1 What is Web Scraping?
Web scraping is extracting data from websites programmatically. Use cases:
- Price monitoring
- Research & data collection
- Lead generation
- Market analysis
- News aggregation

### 1.2 Legal & Ethical Considerations
**Before scraping, check:**
- `robots.txt` file (example.com/robots.txt)
- Website Terms of Service
- Rate limiting (don't overload servers)
- Copyright and data usage rights

**Best Practices:**
- Respect robots.txt
- Add delays between requests
- Use a user agent
- Cache responses when possible

### 1.3 Environment Setup
```bash
# Create virtual environment
python -m venv scraping_env
source scraping_env/bin/activate  # Windows: scraping_env\Scripts\activate

# Install libraries
pip install requests beautifulsoup4 lxml
pip install scrapy selenium playwright
pip install pandas  # for data handling
```

---

## Module 2: HTTP Basics & Requests Library

### 2.1 Understanding HTTP
```python
import requests

# GET request
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # 200 = success
print(response.headers)
print(response.text)

# POST request
data = {'username': 'test', 'password': '12345'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())
```

### 2.2 Headers & User Agents
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get('https://example.com', headers=headers)
```

### 2.3 Handling Sessions & Cookies
```python
# Maintain session across requests
session = requests.Session()
session.get('https://example.com/login')
session.post('https://example.com/login', data={'user': 'me', 'pass': '123'})
response = session.get('https://example.com/dashboard')
```

### 2.4 Error Handling
```python
try:
    response = requests.get('https://example.com', timeout=5)
    response.raise_for_status()  # Raises exception for 4xx/5xx
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## Module 3: HTML Parsing with BeautifulSoup

### 3.1 Basic Parsing
```python
from bs4 import BeautifulSoup
import requests

response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'html.parser')

# Find single element
title = soup.find('h1')
print(title.text)

# Find all elements
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

### 3.2 CSS Selectors
```python
# Using CSS selectors (more powerful)
soup.select('div.content')  # class
soup.select('#main')  # id
soup.select('div > p')  # direct child
soup.select('div p')  # descendant
soup.select('a[href^="https"]')  # attribute starts with

# Example: Scrape article titles
titles = soup.select('article h2.title')
for title in titles:
    print(title.text.strip())
```

### 3.3 Navigating the DOM
```python
# Parent, siblings, children
element = soup.find('div', class_='content')
parent = element.parent
next_sibling = element.next_sibling
children = element.children

# Find by text
soup.find(text='Contact Us')
soup.find('a', string='Click Here')
```

### 3.4 Extracting Data
```python
# Get attributes
link = soup.find('a')
href = link.get('href')  # or link['href']
title = link.get('title', 'No title')  # with default

# Get text
text = link.text  # includes nested elements
text = link.get_text(strip=True)  # remove whitespace
```

---

## Module 4: Real-World Project - News Scraper

### 4.1 Project Structure
```
news_scraper/
├── scraper.py
├── parser.py
├── storage.py
└── main.py
```

### 4.2 Complete Implementation
```python
# scraper.py
import requests
from bs4 import BeautifulSoup
import time

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.base_url = 'https://news.ycombinator.com'
    
    def fetch_page(self, url):
        """Fetch page with error handling"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_articles(self, html):
        """Parse articles from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        
        for item in soup.select('.athing'):
            title_elem = item.select_one('.titleline > a')
            if not title_elem:
                continue
            
            article = {
                'title': title_elem.text,
                'url': title_elem.get('href'),
                'id': item.get('id')
            }
            articles.append(article)
        
        return articles
    
    def scrape(self):
        """Main scraping method"""
        html = self.fetch_page(self.base_url)
        if html:
            articles = self.parse_articles(html)
            return articles
        return []

# main.py
if __name__ == '__main__':
    scraper = NewsScraper()
    articles = scraper.scrape()
    
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   URL: {article['url']}\n")
```

### 4.3 Adding Data Storage
```python
# storage.py
import json
import csv
import pandas as pd

def save_to_json(data, filename='articles.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_to_csv(data, filename='articles.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')

def save_to_excel(data, filename='articles.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
```

---

## Module 5: Advanced Techniques

### 5.1 Handling Pagination
```python
def scrape_multiple_pages(base_url, max_pages=5):
    all_data = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        html = fetch_page(url)
        data = parse_page(html)
        all_data.extend(data)
        
        # Be polite - add delay
        time.sleep(2)
    
    return all_data
```

### 5.2 Rate Limiting
```python
import time
from functools import wraps

def rate_limit(max_calls=10, period=60):
    """Decorator to limit function calls"""
    min_interval = period / max_calls
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(max_calls=5, period=10)
def fetch_url(url):
    return requests.get(url)
```

### 5.3 Concurrent Scraping
```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return response.content

urls = ['https://example.com/page1', 'https://example.com/page2']

# Scrape multiple URLs concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_url, urls)
    
for result in results:
    # Process each result
    pass
```

### 5.4 Handling Dynamic Content (AJAX)
```python
# Method 1: Find the API endpoint
# Open browser DevTools > Network tab > XHR
# Look for JSON responses

import requests

# Direct API call instead of scraping HTML
api_url = 'https://example.com/api/articles?page=1'
response = requests.get(api_url)
data = response.json()
```

---

## Module 6: JavaScript-Heavy Sites with Selenium

### 6.1 Setup & Basic Usage
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.get('https://example.com')

# Wait for element to load
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.content'))
)

# Get page source (now with JS-rendered content)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.quit()
```

### 6.2 Interacting with Pages
```python
# Click elements
button = driver.find_element(By.CSS_SELECTOR, 'button.load-more')
button.click()

# Fill forms
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('python web scraping')
search_box.submit()

# Scroll page
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Take screenshot
driver.save_screenshot('page.png')
```

### 6.3 Headless Mode (Faster)
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
```

---

## Module 7: Scrapy Framework

### 7.1 Create Scrapy Project
```bash
scrapy startproject myproject
cd myproject
scrapy genspider example example.com
```

### 7.2 Spider Implementation
```python
# myproject/spiders/example.py
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://example.com']
    
    def parse(self, response):
        # Extract data
        for article in response.css('article'):
            yield {
                'title': article.css('h2::text').get(),
                'link': article.css('a::attr(href)').get(),
                'date': article.css('.date::text').get(),
            }
        
        # Follow pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

### 7.3 Run Spider
```bash
# Run and save to JSON
scrapy crawl example -o output.json

# Run with custom settings
scrapy crawl example -s CONCURRENT_REQUESTS=1 -s DOWNLOAD_DELAY=2
```

### 7.4 Scrapy Settings
```python
# settings.py
BOT_NAME = 'myproject'

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 1

USER_AGENT = 'Mozilla/5.0 (compatible; MyBot/1.0)'

# Enable AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
```

---

## Module 8: Anti-Scraping Countermeasures

### 8.1 Rotating User Agents
```python
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
]

headers = {'User-Agent': random.choice(USER_AGENTS)}
response = requests.get(url, headers=headers)
```

### 8.2 Using Proxies
```python
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080',
}

response = requests.get(url, proxies=proxies)
```

### 8.3 Handling CAPTCHAs
- Use CAPTCHA solving services (2Captcha, Anti-Captcha)
- Consider if scraping is appropriate
- Look for alternative data sources (APIs)

---

## Module 9: Best Practices & Optimization

### 9.1 Caching Responses
```python
import hashlib
import os

def cache_response(url, content):
    """Cache HTML responses"""
    cache_dir = 'cache'
    os.makedirs(cache_dir, exist_ok=True)
    
    filename = hashlib.md5(url.encode()).hexdigest()
    filepath = os.path.join(cache_dir, filename)
    
    with open(filepath, 'wb') as f:
        f.write(content)

def get_cached_response(url):
    """Get cached response if exists"""
    cache_dir = 'cache'
    filename = hashlib.md5(url.encode()).hexdigest()
    filepath = os.path.join(cache_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return f.read()
    return None
```

### 9.2 Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info('Starting scraper')
logger.error('Failed to fetch URL', exc_info=True)
```

### 9.3 Data Validation
```python
from typing import Dict, Optional

def validate_article(article: Dict) -> bool:
    """Validate scraped article data"""
    required_fields = ['title', 'url']
    
    # Check required fields exist
    for field in required_fields:
        if field not in article or not article[field]:
            logger.warning(f"Missing field: {field}")
            return False
    
    # Validate URL format
    if not article['url'].startswith('http'):
        logger.warning(f"Invalid URL: {article['url']}")
        return False
    
    return True
```

---

## Module 10: Complete E-commerce Scraper Project

### 10.1 Product Scraper
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

class ProductScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.products = []
    
    def scrape_product(self, url):
        """Scrape single product page"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            product = {
                'name': soup.select_one('h1.product-title').text.strip(),
                'price': self.extract_price(soup),
                'rating': self.extract_rating(soup),
                'availability': soup.select_one('.availability').text.strip(),
                'url': url,
                'scraped_at': datetime.now().isoformat()
            }
            
            return product
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def extract_price(self, soup):
        """Extract and clean price"""
        price_elem = soup.select_one('.price')
        if price_elem:
            price_text = price_elem.text.strip()
            # Remove currency symbols and convert to float
            import re
            price = re.sub(r'[^\d.]', '', price_text)
            return float(price) if price else None
        return None
    
    def extract_rating(self, soup):
        """Extract rating"""
        rating_elem = soup.select_one('.rating')
        if rating_elem:
            rating_text = rating_elem.get('aria-label', '')
            import re
            match = re.search(r'(\d+\.?\d*)', rating_text)
            return float(match.group(1)) if match else None
        return None
    
    def scrape_category(self, category_url, max_pages=5):
        """Scrape all products in a category"""
        for page in range(1, max_pages + 1):
            url = f"{category_url}?page={page}"
            print(f"Scraping page {page}...")
            
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all product links
            product_links = soup.select('a.product-link')
            
            for link in product_links:
                product_url = link.get('href')
                product = self.scrape_product(product_url)
                
                if product:
                    self.products.append(product)
                
                time.sleep(1)  # Be polite
            
            # Check if there's a next page
            if not soup.select_one('a.next-page'):
                break
            
            time.sleep(2)
    
    def save_results(self, filename='products.csv'):
        """Save scraped data"""
        df = pd.DataFrame(self.products)
        df.to_csv(filename, index=False)
        print(f"Saved {len(self.products)} products to {filename}")

# Usage
if __name__ == '__main__':
    scraper = ProductScraper()
    scraper.scrape_category('https://example.com/electronics', max_pages=3)
    scraper.save_results()
```

---

## Module 11: Troubleshooting & Debugging

### 11.1 Common Issues

**Problem: Empty results**
```python
# Check if page loaded
print(response.status_code)
print(len(response.content))

# Save HTML to file for inspection
with open('debug.html', 'w') as f:
    f.write(response.text)

# Check if selector is correct
elements = soup.select('your-selector')
print(f"Found {len(elements)} elements")
```

**Problem: Blocked by website**
- Check robots.txt
- Add proper User-Agent
- Reduce request rate
- Use proxies
- Check if site requires JavaScript (use Selenium)

**Problem: Encoding issues**
```python
# Specify encoding
response.encoding = 'utf-8'
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
```

### 11.2 Testing Selectors
Use browser console to test CSS selectors:
```javascript
// In browser console
document.querySelectorAll('your-selector')
```

---

## Module 12: Resources & Next Steps

### 12.1 Additional Libraries
- **httpx**: Modern async HTTP client
- **aiohttp**: Async HTTP requests
- **lxml**: Faster HTML parsing
- **parsel**: Scrapy's extraction library (standalone)
- **newspaper3k**: Article extraction

### 12.2 Learning Resources
- Scrapy documentation
- Real Python web scraping tutorials
- ScrapingHub blog
- r/webscraping subreddit

### 12.3 Practice Projects
1. **Job Board Scraper**: Track job postings
2. **Real Estate Monitor**: Track property prices
3. **Social Media Analyzer**: Scrape public posts
4. **Price Tracker**: Monitor product prices
5. **News Aggregator**: Collect news from multiple sources

### 12.4 Legal Considerations Checklist
- [ ] Read website's Terms of Service
- [ ] Check robots.txt compliance
- [ ] Verify data usage rights
- [ ] Consider using official APIs first
- [ ] Implement rate limiting
- [ ] Respect user privacy
- [ ] Add proper attribution

---

## Final Project: Multi-Site News Aggregator

Build a news aggregator that:
1. Scrapes multiple news sites
2. Extracts article metadata (title, author, date, summary)
3. Stores data in SQLite database
4. Removes duplicates
5. Generates daily reports
6. Sends email notifications

This combines all skills learned:
- HTTP requests
- HTML parsing
- Data storage
- Error handling
- Scheduling (using `schedule` library)
- Email sending (using `smtplib`)

**Good luck with your web scraping journey!**
