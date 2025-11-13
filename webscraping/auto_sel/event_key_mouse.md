**Browser Events, Keyboard & Mouse**

**Browser Navigation:**
- `driver.get("url")` - Navigate to URL
- `driver.back()` - Go back
- `driver.forward()` - Go forward
- `driver.refresh()` - Reload page

**Keyboard Actions:**

```python
from selenium.webdriver.common.keys import Keys

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)  # Press Enter

# Special keys
search_box.send_keys(Keys.BACKSPACE)
search_box.send_keys(Keys.TAB)
search_box.send_keys(Keys.CONTROL, "a")  # Ctrl+A (Select all)
search_box.send_keys(Keys.CONTROL, "c")  # Ctrl+C (Copy)
```

**Mouse Actions:**

```python
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "menu")

# Hover over element
ActionChains(driver).move_to_element(element).perform()

# Double click
ActionChains(driver).double_click(element).perform()

# Right click
ActionChains(driver).context_click(element).perform()

# Drag and drop
source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")
ActionChains(driver).drag_and_drop(source, target).perform()

# Click and hold
ActionChains(driver).click_and_hold(element).perform()
ActionChains(driver).release(element).perform()
```

**Example - Hover menu:**

```python
from selenium.webdriver.common.action_chains import ActionChains

driver.get("https://example.com")

# Hover over menu to reveal dropdown
menu = driver.find_element(By.ID, "products-menu")
ActionChains(driver).move_to_element(menu).perform()

# Click submenu item that appears
submenu = driver.find_element(By.LINK_TEXT, "Laptops")
submenu.click()
```