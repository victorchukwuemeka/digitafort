**Interacting with Elements**

Once you find an element, you can interact with it:

**Common Actions:**

- **`.click()`** - Click the element
- **`.send_keys("text")`** - Type text into input fields
- **`.clear()`** - Clear text from input fields
- **`.submit()`** - Submit a form
- **`.text`** - Get the visible text
- **`.get_attribute("attribute_name")`** - Get attribute value (href, src, etc.)

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find search box and type
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

# Submit the search
search_box.submit()

# Or click a button instead
# button = driver.find_element(By.NAME, "btnK")
# button.click()

# Get text from a result
result = driver.find_element(By.TAG_NAME, "h3")
print(result.text)

driver.quit()
```

This finds Google's search box, types "Selenium Python", submits the search, and prints the first result heading.