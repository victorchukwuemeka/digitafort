
# Selenium Automation Roadmap (Python)

## 1️⃣ **Introduction**

* What Selenium is and why use it
* Browser automation vs web scraping
* Dynamic vs static websites

---

## 2️⃣ **Setup**

* Install Python & pip
* Install Selenium library:

```bash
pip install selenium
```

* Download browser drivers:

  * Chrome → ChromeDriver
  * Firefox → GeckoDriver
* Optional: Headless browsers (Chrome/Firefox headless mode)

---

## 3️⃣ **Basic Browser Operations**

* Launch a browser:

```python
driver = webdriver.Chrome()
```

* Open a URL: `driver.get("https://example.com")`
* Close a browser: `driver.quit()` or `driver.close()`
* Navigate: `back()`, `forward()`, `refresh()`

---

## 4️⃣ **Finding Elements**

* By ID, Name, Class, Tag, CSS Selector, XPath

```python
element = driver.find_element(By.ID, "element_id")
elements = driver.find_elements(By.CLASS_NAME, "class_name")
```

* Difference between `find_element` (single) vs `find_elements` (list)

---

## 5️⃣ **Interacting with Elements**

* Click buttons: `element.click()`
* Send text: `element.send_keys("text")`
* Clear input: `element.clear()`
* Submit forms: `element.submit()`

---

## 6️⃣ **Advanced Selectors**

* CSS Selectors
* XPath expressions
* Attribute matching, contains, starts-with, etc.
* Useful when IDs/classes aren’t available

---

## 7️⃣ **Handling Browser Events**

* Waits:

  * **Implicit Wait**: waits globally for elements to appear

    ```python
    driver.implicitly_wait(10)
    ```
  * **Explicit Wait**: waits for a specific condition

    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element_id")))
    ```
* Alerts, pop-ups, and confirmations
* Switching between windows/tabs
* Switching to frames/iframes

---

## 8️⃣ **Working with Forms**

* Input text fields
* Radio buttons & checkboxes
* Dropdowns (Select class)

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option 1")
```

---

## 9️⃣ **Keyboard & Mouse Actions**

* ActionChains for advanced interactions:

  * Hover over elements
  * Drag & drop
  * Right click / double click

```python
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
```

---

## 🔟 **Scraping with Selenium**

* Get text: `element.text`
* Get attributes: `element.get_attribute("href")`
* Loop through multiple elements and extract data
* Export scraped data (CSV, JSON, etc.)

---

## 1️⃣1️⃣ **Handling Dynamic Websites**

* Infinite scroll pages
* JavaScript-generated content
* Using waits to ensure elements load before interaction

---

## 1️⃣2️⃣ **Taking Screenshots & Logging**

* Full page screenshot: `driver.save_screenshot("screenshot.png")`
* Element screenshot: `element.screenshot("element.png")`
* Logging actions/errors for debugging

---

## 1️⃣3️⃣ **Headless Mode & Performance**

* Run browser without GUI (faster)

```python
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
```

---

## 1️⃣4️⃣ **Testing & Automation Frameworks**

* Combine Selenium with **pytest** or **unittest** for automation tests
* Page Object Model (POM) for scalable automation
* CI/CD integration for automated testing

---

## 1️⃣5️⃣ **Best Practices**

* Use **explicit waits** over implicit waits
* Avoid hardcoding element locators (use variables/constants)
* Keep scripts modular and reusable
* Handle exceptions gracefully (`try/except`)
* Respect website terms of service and avoid overloading servers

---

### ✅ Optional Advanced Topics

* Mobile browser automation (Appium + Selenium)
* Captcha handling (third-party services)
* Multi-tab/window automation
* Headless browser in CI/CD pipelines

---

