# Selenium & Python — Classroom Lesson Guide
**Topic:** Web Automation from Scratch  
**Duration:** ~90 min | **Audience:** Beginners  

---

## What to Tell Students Before You Start

> "Today we are going to write Python code that controls a real browser — opens websites, clicks buttons, reads data — automatically. No touching the mouse, no copying and pasting. Pure code."

---

## PART 1 — What is Selenium? (10 min)

### Say this:
> "Selenium is a tool that lets your Python script drive a browser like a human would. It was originally built for testing websites, but people use it for scraping data and automating boring web tasks too."

### Draw this on the board:
```
Your Python Script  →  WebDriver  →  Chrome / Firefox
```

> "Your script gives instructions. WebDriver translates them into browser actions. That's it."

### Key points to hit:
- Selenium is **open source** and free
- Works with Chrome, Firefox, Edge
- We use **Python** to write the instructions
- `webdriver-manager` handles driver downloads automatically — no manual setup

---

## PART 2 — Setup (10 min)

### Run this in terminal (show students):
```bash
pip install selenium webdriver-manager
```

### Write this on screen together:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com")

print(driver.title)

driver.quit()
```

### Say this:
> "`driver.get()` is like typing a URL and pressing Enter.  
> `driver.title` reads the page title.  
> `driver.quit()` closes the browser — always do this at the end."

### Run it. Expected output:
```
Quotes to Scrape
```

> "Chrome opened by itself, visited the site, printed the title, closed. That is Selenium."

---

## PART 3 — Finding Elements (20 min)

### Say this:
> "Everything in Selenium starts with finding an element on the page. Think of it like telling someone: 'grab the red button in the top-right corner.' We describe what we want, Selenium finds it."

### Show students how to inspect:
- Open `https://quotes.toscrape.com` in Chrome
- Right-click any quote → **Inspect**
- Point out: tag names, class names, IDs

### The 4 locators they must know:

| Locator | Use When |
|---|---|
| `By.ID` | Element has a unique id attribute |
| `By.CLASS_NAME` | Element has a class |
| `By.CSS_SELECTOR` | Flexible — works for almost anything |
| `By.XPATH` | Complex structures, last resort |

### Write this together:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com")

# find ONE element
first_quote = driver.find_element(By.CLASS_NAME, "text")
print(first_quote.text)

# find ALL elements
all_quotes = driver.find_elements(By.CLASS_NAME, "text")
print(f"Found {len(all_quotes)} quotes")

driver.quit()
```

### Say this:
> "`find_element` — singular — crashes if nothing is found.  
> `find_elements` — plural — returns an empty list if nothing is found. Safer."

---

## PART 4 — Interacting with Elements (20 min)

### Say this:
> "Finding elements is step one. Step two is doing something with them — clicking, typing, reading."

### The actions they need:

| Action | Method |
|---|---|
| Click a button | `.click()` |
| Type into a field | `.send_keys("text")` |
| Clear a field | `.clear()` |
| Read visible text | `.text` |
| Read an attribute | `.get_attribute("href")` |

### Write this together (login example):
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

print(driver.current_url)

driver.quit()
```

### Run it. Say this:
> "It typed. It clicked. It submitted the form. `current_url` tells us where we landed after the click."

---

## PART 5 — Waits (15 min)

### Say this:
> "This is where most beginners break their scripts. Real websites load content dynamically — the element you want might not exist yet when Selenium looks for it."

### Show the problem:
```python
# This can crash — Selenium looks before the page loads
driver.find_element(By.ID, "something")
```

### Two types of waits:

**Implicit Wait** — tells Selenium to wait globally before throwing an error:
```python
driver.implicitly_wait(5)  # waits up to 5 seconds for any element
```

**Explicit Wait** — waits for a specific condition (use this in real projects):
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text")))
```

### Say this:
> "Explicit wait is the professional approach. You say exactly what you're waiting for and how long to wait. Never use `time.sleep()` — it's lazy and breaks on slow connections."

---

## PART 6 — Putting It All Together (15 min)

### Say this:
> "Let's write one complete script that uses everything — open browser, wait, find elements, extract data."

### Write the final script together:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for q in quotes:
    text = q.find_element(By.CLASS_NAME, "text").text
    author = q.find_element(By.CLASS_NAME, "author").text
    print(f"{author}: {text}")

driver.quit()
```

### Run it. Say this:
> "Every quote, every author — clean and structured. Notice we searched inside each quote element to find the text and author. Elements can be searched within elements."

---

## Wrap Up (5 min)

### What students learned today:
1. What Selenium is and how it works
2. How to set up and open a browser with code
3. How to find elements — by ID, class, CSS selector
4. How to interact — type, click, read
5. How to wait properly so scripts don't break

### Tease next lesson:
> "Next class we cover Page Object Model — how to structure your automation code like a professional so it doesn't turn into a mess as projects grow."

---

## Quick Reference Card

```python
# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate
driver.get("https://example.com")
driver.back()
driver.refresh()

# Find
driver.find_element(By.ID, "id")
driver.find_element(By.CLASS_NAME, "class")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
driver.find_elements(By.CLASS_NAME, "item")  # returns list

# Interact
element.click()
element.send_keys("text")
element.clear()
element.text
element.get_attribute("href")

# Wait
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn")))

# Close
driver.quit()
```