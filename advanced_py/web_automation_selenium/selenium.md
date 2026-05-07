# Selenium & Python — Web Automation
**Topic:** Web Automation from Scratch  
**Duration:** ~90 min

---

## What is Selenium?

Selenium is a tool that lets your Python script drive a real browser — open websites, click buttons, fill forms, and read data — automatically.

```
Your Python Script  →  WebDriver  →  Chrome / Firefox
```

- Open source and free
- Works with Chrome, Firefox, Edge
- `webdriver-manager` handles everything automatically — no manual driver setup

---

## Setup

```bash
pip install selenium webdriver-manager
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com")

print(driver.title)   # Quotes to Scrape

driver.quit()
```

| Method | What it does |
|---|---|
| `driver.get(url)` | Open a URL |
| `driver.title` | Read the page title |
| `driver.current_url` | Read the current URL |
| `driver.quit()` | Close the browser — always do this |

---

## Finding Elements

To interact with a page, you first need to find the element you want.

```python
from selenium.webdriver.common.by import By

# Find ONE element — crashes if not found
element = driver.find_element(By.CLASS_NAME, "text")

# Find ALL elements — returns empty list if not found
elements = driver.find_elements(By.CLASS_NAME, "text")
```

### Locator strategies

| Locator | Example | Use When |
|---|---|---|
| `By.ID` | `By.ID, "username"` | Element has a unique id |
| `By.CLASS_NAME` | `By.CLASS_NAME, "quote"` | Element has a class |
| `By.CSS_SELECTOR` | `By.CSS_SELECTOR, "input[type='submit']"` | Flexible targeting |
| `By.XPATH` | `By.XPATH, "//button[text()='Login']"` | Complex structures |

> **Tip:** Right-click any element in Chrome → **Inspect** to see its tag, class, and id.

---

## Interacting with Elements

```python
element.click()                    # Click a button or link
element.send_keys("hello@email.com")  # Type into a field
element.clear()                    # Clear existing text
element.text                       # Read visible text
element.get_attribute("href")      # Read an HTML attribute
```

### Example — fill and submit a login form:

```python
driver.get("https://quotes.toscrape.com/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

print(driver.current_url)
```

---

## Waits

Real websites load dynamically. If Selenium looks for an element before it loads, your script crashes.

**Implicit Wait** — global wait applied to every element lookup:
```python
driver.implicitly_wait(5)
```

**Explicit Wait** — wait for a specific condition (recommended):
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

# Wait until element exists
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text")))

# Wait until element is clickable
button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
```

> Never use `time.sleep()` — it wastes time and breaks on slow connections.

---

## Full Example

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

---

## Quick Reference

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
driver.find_element(By.CSS_SELECTOR, "div.card > a")
driver.find_elements(By.CLASS_NAME, "item")        # returns a list

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