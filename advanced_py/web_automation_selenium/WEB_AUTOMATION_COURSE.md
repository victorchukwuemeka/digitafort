# Web Automation with Selenium & Python — Complete Course with Exercises

**Browser:** Firefox (GeckoDriver)  
**How to use this course:** Each chapter has a detailed explanation followed by a **complete, runnable Python exercise**. Save the exercise as `.py` and run it.

---

## Chapter 0: Setup

```bash
pip install selenium webdriver-manager
```

`webdriver-manager` automatically downloads the correct GeckoDriver for your Firefox version. No manual PATH setup needed.

---

## Chapter 1: Your First Automation Script

### Explanation
Every Selenium script follows the same pattern:
1. **Create a driver** — this opens a Firefox window.
2. **Navigate** — `driver.get()` goes to a URL.
3. **Do something** — find elements, click, type.
4. **Close** — `driver.quit()` closes the browser.

The `Service(GeckoDriverManager().install())` part handles downloading and locating the Firefox driver binary.

### Exercise — Run this code

```python
# exercise_01_first_script.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://www.google.com")
    print(f"Page title: {driver.title}")
    print(f"Current URL: {driver.current_url}")
finally:
    driver.quit()
```

**What you'll learn:** Opening Firefox, navigating, reading title/URL, proper cleanup with `try/finally`.

---

## Chapter 2: Locating Elements — ID, Name, Class

### Explanation
Before you can interact with anything on a page, you must **find it**. Selenium gives you 8 strategies. The three most common are:

| Strategy | Example | Description |
|---|---|---|
| `By.ID` | `By.ID, "username"` | Fastest — uses the `id` attribute |
| `By.NAME` | `By.NAME, "email"` | Good for form inputs |
| `By.CLASS_NAME` | `By.CLASS_NAME, "btn"` | Uses the `class` attribute |

- `find_element()` returns the **first** match (raises error if not found).
- `find_elements()` returns a **list** of all matches (empty list if none found).

### Exercise — Run this code

```python
# exercise_02_locators_basic.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # By.ID — fastest and most reliable
    username = driver.find_element(By.ID, "username")
    print(f"Username input found: {username.tag_name}")

    # By.NAME — useful for form fields
    password = driver.find_element(By.NAME, "password")
    print(f"Password input found: {password.tag_name}")

    # By.CLASS_NAME — elements by CSS class
    button = driver.find_element(By.CLASS_NAME, "radius")
    print(f"Button found: {button.text}")

    # find_elements — returns a list
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Total <input> elements on page: {len(all_inputs)}")

finally:
    driver.quit()
```

**Expected output:**
```
Username input found: input
Password input found: input
Button found: Login
Total <input> elements on page: 2
```

---

## Chapter 3: Locating Elements — CSS Selectors

### Explanation
CSS selectors are the most powerful and readable way to locate elements. They use the same syntax as CSS styling.

```
Pattern           Matches
#username         element with id="username"
.btn              element with class="btn"
input[type="text"]  <input type="text">
a[href*="login"]  <a> whose href contains "login"
form > input      direct child
ul li             descendant
li:first-child    first <li> in a parent
li:nth-child(2)   second <li>
```

**Why learn CSS selectors?** They are faster than XPath, more flexible than ID/name, and work great with modern web apps.

### Exercise — Run this code

```python
# exercise_03_locators_css.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # By attribute
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print(f"Submit button text: '{submit.text}'")

    # By class + tag
    icon = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in")
    print(f"Icon classes: {icon.get_attribute('class')}")

    # By ID prefix with #
    username = driver.find_element(By.CSS_SELECTOR, "#username")
    username.send_keys("tomsmith")

    # By attribute containing text
    label = driver.find_element(By.CSS_SELECTOR, "label[for*='pass']")
    print(f"Password label: '{label.text}'")

    # Multiple elements
    all_labels = driver.find_elements(By.CSS_SELECTOR, "label")
    print(f"Labels on page: {len(all_labels)}")
    for lbl in all_labels:
        print(f"  - '{lbl.text}'")

finally:
    driver.quit()
```

---

## Chapter 4: Locating Elements — XPath

### Explanation
XPath is the most flexible locator. Use it when CSS selectors can't express the relationship you need.

```
Expression                         Meaning
//input[@id='username']            <input id="username"> anywhere
//button[text()='Login']           <button> with exact text "Login"
//button[contains(text(),'Log')]   <button> text contains "Log"
//*[@data-testid='submit']         any element with data-testid
//div[contains(@class,'error')]    <div> whose class contains "error"
//input[@type='submit']/..         parent of the input
``` 

**Rule:** Try `By.ID` first → `By.CSS_SELECTOR` → `By.XPATH` last.

### Exercise — Run this code

```python
# exercise_04_locators_xpath.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # By text content
    heading = driver.find_element(By.XPATH, "//h2[text()='Login Page']")
    print(f"Heading: '{heading.text}'")

    # contains() — partial text match
    flash = driver.find_element(By.XPATH, "//div[contains(@class, 'flash')]")
    print(f"Flash element class: {flash.get_attribute('class')}")

    # By attribute + tag
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    print(f"Submit text: '{submit.text}'")

    # Finding with OR condition
    btn = driver.find_element(By.XPATH, "//button[@type='submit' or @name='submit']")
    print(f"Button found via OR: '{btn.text}'")

    # parent/child
    form = driver.find_element(By.XPATH, "//input[@id='username']/../..")
    print(f"Form tag: {form.tag_name}")

    # count matches
    all = driver.find_elements(By.XPATH, "//*[@id]")
    print(f"Elements with an 'id' attribute: {len(all)}")

finally:
    driver.quit()
```

---

## Chapter 5: Interacting with Elements

### Explanation
Once you find an element, you can:

| Method | What it does |
|---|---|
| `.click()` | Clicks the element |
| `.send_keys("text")` | Types text into a field |
| `.send_keys(Keys.RETURN)` | Presses the Enter key |
| `.clear()` | Clears a text field |
| `.text` | Gets visible text |
| `.get_attribute("href")` | Gets an attribute value |
| `.is_displayed()` | True if visible |
| `.is_enabled()` | True if not disabled |
| `.is_selected()` | True if checkbox/radio is checked |

### Exercise — Run this code

```python
# exercise_05_interactions.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Type into fields
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    # Check states before clicking
    print(f"Button enabled? {button.is_enabled()}")
    print(f"Button displayed? {button.is_displayed()}")
    print(f"Username value: '{username.get_attribute('value')}'")

    # Click the button
    button.click()

    # Read the success message
    flash = driver.find_element(By.ID, "flash")
    print(f"Flash message: '{flash.text.strip()}'")

    # Get attribute
    logout_link = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    print(f"Logout href: {logout_link.get_attribute('href')}")

    # Current page info
    print(f"After login URL: {driver.current_url}")
    print(f"Page title: {driver.title}")

finally:
    driver.quit()
```

---

## Chapter 6: Waits — The Most Important Skill

### Explanation
Web pages load content dynamically. If you try to find an element before it exists, your script crashes. **Never use `time.sleep()`** — it's slow and brittle.

**Implicit Wait** — sets a global timeout for `find_element`:
```python
driver.implicitly_wait(10)  # poll for up to 10 seconds
```

**Explicit Wait (BEST)** — waits for a specific condition on a specific element:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
el = wait.until(EC.presence_of_element_located((By.ID, "username")))
```

Common conditions:
| `EC.xxx` | Waits until... |
|---|---|
| `presence_of_element_located` | Element exists in DOM |
| `visibility_of_element_located` | Element is visible on page |
| `element_to_be_clickable` | Element is visible AND enabled |
| `text_to_be_present_in_element` | Element contains specific text |
| `invisibility_of_element_located` | Element disappears (loading spinner) |
| `alert_is_present` | An alert dialog is open |

### Exercise — Run this code

```python
# exercise_06_waits.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Click start — content loads dynamically after this
    driver.find_element(By.CSS_SELECTOR, "button").click()

    # Explicit wait for the hidden element to become visible
    wait = WebDriverWait(driver, 10)
    hello = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    print(f"Dynamically loaded text: '{hello.text}'")

    # ── Also test: wait and fail gracefully ──
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "button").click()

    try:
        # This waits up to 10 seconds
        result = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        finish_el = driver.find_element(By.ID, "finish")
        print(f"Result: '{finish_el.text}'")
    except TimeoutException:
        print("Timed out waiting for content!")

finally:
    driver.quit()
```

---

## Chapter 7: Navigation, Windows & Tabs

### Explanation
Selenium can open new tabs, switch between windows, go back/forward, and resize the browser.

Key methods:
```python
driver.back()           # browser back button
driver.forward()        # browser forward button
driver.refresh()        # refresh page
driver.window_handles   # list of all open window handles
driver.switch_to.window(handle)  # switch to a specific window
driver.close()          # close current tab/window
driver.maximize_window()
```

### Exercise — Run this code

```python
# exercise_07_navigation.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Open page with "Click Here" link that opens a new window
    driver.get("https://the-internet.herokuapp.com/windows")
    main_window = driver.current_window_handle
    print(f"Main window handle: {main_window}")
    print(f"Main window title: '{driver.title}'")

    # Click link — opens new window
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # Wait for the new window to exist
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))

    # Switch to the new window
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    print(f"New window title: '{driver.title}'")
    print(f"New window text: '{driver.find_element(By.TAG_NAME, 'h3').text}'")

    # Close new window and go back to main
    driver.close()
    driver.switch_to.window(main_window)
    print(f"Back to main, title: '{driver.title}'")

    # Navigation buttons
    driver.get("https://the-internet.herokuapp.com")
    print(f"After navigation: {driver.title}")

    driver.back()
    print(f"After back: {driver.title}")

    driver.forward()
    print(f"After forward: {driver.title}")

finally:
    driver.quit()
```

---

## Chapter 8: Dropdowns (Select class)

### Explanation
HTML `<select>` elements need special handling. Use the `Select` class.

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(element)
dropdown.select_by_visible_text("Option 1")  # by what the user sees
dropdown.select_by_value("1")                # by the value attribute
dropdown.select_by_index(0)                  # by position (0-based)
dropdown.options                             # list of all <option> elements
dropdown.first_selected_option               # currently selected
```

### Exercise — Run this code

```python
# exercise_08_dropdown.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    # List all options
    print("Available options:")
    for opt in dropdown.options:
        selected = " [SELECTED]" if opt.is_selected() else ""
        print(f"  value='{opt.get_attribute('value')}' -> '{opt.text}'{selected}")

    # Select by visible text
    dropdown.select_by_visible_text("Option 1")
    selected = dropdown.first_selected_option
    print(f"\nSelected: '{selected.text}' (value='{selected.get_attribute('value')}')")

    # Select by value attribute
    dropdown.select_by_value("2")
    selected = dropdown.first_selected_option
    print(f"After select_by_value('2'): '{selected.text}'")

finally:
    driver.quit()
```

---

## Chapter 9: Alerts, Frames, and iFrames

### Explanation

**Alerts** — browser popups (OK/Cancel/prompt):
```python
alert = driver.switch_to.alert
alert.text        # read message
alert.accept()    # click OK
alert.dismiss()   # click Cancel
alert.send_keys("text")  # type in prompt alert
```

**Frames/iFrames** — embedded documents:
```python
driver.switch_to.frame("frame-name-or-id")
driver.switch_to.frame(0)              # by index
driver.switch_to.frame(element)        # by element
driver.switch_to.default_content()     # back to main page
```

### Exercise — Run this code

```python
# exercise_09_alerts_frames.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # ═══ Alerts ═══
    print("═══ Alerts ═══")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS Alert
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"Alert text: '{alert.text}'")
    alert.accept()
    result = driver.find_element(By.ID, "result").text
    print(f"After accept: '{result}'")

    # JS Confirm — dismiss
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.dismiss()
    result = driver.find_element(By.ID, "result").text
    print(f"After dismiss: '{result}'")

    # JS Prompt — type text
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.send_keys("Hello from Selenium!")
    alert.accept()
    result = driver.find_element(By.ID, "result").text
    print(f"After prompt: '{result}'")

    # ═══ Frames ═══
    print("\n═══ Frames ═══")
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Switch to top frame
    driver.switch_to.frame("frame-top")
    # Switch to nested left frame
    driver.switch_to.frame("frame-left")
    left_body = driver.find_element(By.TAG_NAME, "body")
    print(f"Left frame content: '{left_body.text}'")
    driver.switch_to.default_content()

    # Switch to bottom frame
    driver.switch_to.frame("frame-bottom")
    bottom_body = driver.find_element(By.TAG_NAME, "body")
    print(f"Bottom frame content: '{bottom_body.text}'")

finally:
    driver.quit()
```

---

## Chapter 10: ActionChains — Mouse & Keyboard

### Explanation
`ActionChains` lets you perform complex interactions like hover, drag-and-drop, double-click, and right-click.

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(element).perform()     # hover
actions.double_click(element).perform()        # double click
actions.context_click(element).perform()       # right click
actions.drag_and_drop(source, target).perform()
actions.click_and_hold(el).move_to_element(el2).release().perform()
```

Multiple actions can be chained:
```python
actions \
    .move_to_element(menu) \
    .click() \
    .pause(0.5) \
    .send_keys("hello") \
    .perform()
```

### Exercise — Run this code

```python
# exercise_10_action_chains.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # ═══ Hover ═══
    print("═══ Hover ═══")
    driver.get("https://the-internet.herokuapp.com/hovers")
    actions = ActionChains(driver)

    avatar = driver.find_element(By.CSS_SELECTOR, ".figure")
    actions.move_to_element(avatar).perform()

    caption = driver.find_element(By.CSS_SELECTOR, ".figcaption h5")
    print(f"After hover — caption: '{caption.text}'")

    # ═══ Drag and Drop ═══
    print("\n═══ Drag and Drop ═══")
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")

    actions.drag_and_drop(source, target).perform()

    source_header = driver.find_element(By.CSS_SELECTOR, "#column-a header")
    target_header = driver.find_element(By.CSS_SELECTOR, "#column-b header")
    print(f"Column A now: '{source_header.text}'")
    print(f"Column B now: '{target_header.text}'")

    # ═══ Double Click ═══
    print("\n═══ Double Click ═══")
    driver.get("https://the-internet.herokuapp.com/context_menu")
    box = driver.find_element(By.ID, "hot-spot")

    actions.context_click(box).perform()
    alert = driver.switch_to.alert
    print(f"Context menu alert: '{alert.text}'")
    alert.accept()

    # ═══ Keyboard Combinations ═══
    print("\n═══ Keyboard ═══")
    driver.get("https://the-internet.herokuapp.com/key_presses")

    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.CONTROL, "a")  # Select all
    result = driver.find_element(By.ID, "result")
    print(f"Key result: '{result.text}'")

finally:
    driver.quit()
```

---

## Chapter 11: JavaScript Execution

### Explanation
Sometimes Selenium's API can't do what you need. Use `execute_script()` to run JavaScript directly.

```python
# Scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Click a hidden element
driver.execute_script("arguments[0].click();", element)

# Get data
title = driver.execute_script("return document.title;")

# Change style (for debugging)
driver.execute_script("arguments[0].style.border = '3px solid red';", element)

# Remove an attribute
driver.execute_script("arguments[0].removeAttribute('disabled');", element)

# Scroll to element
driver.execute_script("arguments[0].scrollIntoView(true);", element)
```

`arguments[0]`, `arguments[1]`, etc. refer to the Python objects you pass after the JS string.

### Exercise — Run this code

```python
# exercise_11_javascript.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/large")

    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    scroll_y = driver.execute_script("return window.scrollY;")
    print(f"Scrolled {scroll_y}px down")

    # Get page info via JS
    title = driver.execute_script("return document.title;")
    url = driver.execute_script("return document.URL;")
    domain = driver.execute_script("return document.domain;")
    print(f"Title: '{title}'")
    print(f"URL: {url}")
    print(f"Domain: {domain}")

    # Highlight an element
    table = driver.find_element(By.ID, "large-table")
    driver.execute_script(
        "arguments[0].style.border = '5px solid red'; "
        "arguments[0].style.background = 'yellow';",
        table
    )
    print("Table highlighted with red border and yellow background")

    # Get element dimensions via JS
    rect = driver.execute_script(
        "var r = arguments[0].getBoundingClientRect(); "
        "return {left: r.left, top: r.top, width: r.width, height: r.height};",
        table
    )
    print(f"Table position/size: {rect}")

    # Count all images
    img_count = driver.execute_script("return document.images.length;")
    print(f"Images on page: {img_count}")

    # Modify page (add text to body)
    driver.execute_script(
        "var d = document.createElement('div');"
        "d.id = 'injected-by-selenium';"
        "d.style.padding = '20px';"
        "d.style.background = 'lightgreen';"
        "d.textContent = 'This was added by Selenium!';"
        "document.body.prepend(d);"
    )
    injected = driver.find_element(By.ID, "injected-by-selenium")
    print(f"Injected div text: '{injected.text}'")

finally:
    driver.quit()
```

---

## Chapter 12: File Upload

### Explanation
File upload is surprisingly simple: just send the absolute file path to the `<input type="file">` element. No need to click anything.

```python
upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
upload.send_keys("/path/to/file.pdf")
```

The browser handles the file dialog automatically. This works with any `<input type="file">`.

### Exercise — Run this code

```python
# exercise_12_file_upload.py
import tempfile
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Create a temporary test file
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", prefix="selenium_test_", delete=False
    ) as f:
        f.write("This file was uploaded by Selenium!\n")
        f.write("Line 2 of the test file.\n")
        test_file_path = f.name

    print(f"Created test file: {test_file_path}")

    driver.get("https://the-internet.herokuapp.com/upload")

    # Find the file input and send the file path
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys(test_file_path)
    print(f"Sent file path to input")

    # Click Upload
    driver.find_element(By.ID, "file-submit").click()

    # Read result
    uploaded_files = driver.find_element(By.ID, "uploaded-files")
    print(f"Uploaded file(s): '{uploaded_files.text}'")

    assert "selenium_test_" in uploaded_files.text
    print("SUCCESS: File upload verified!")

finally:
    driver.quit()
    # Clean up temp file
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
        print(f"Cleaned up: {test_file_path}")
```

---

## Chapter 13: Page Object Model (POM)

### Explanation
POM is the industry standard pattern for organizing automation code. Each web page gets its own class. The class stores locators as class constants and provides methods that represent page actions.

Benefits:
- If a page changes, you update only one class.
- Tests become readable: `login_page.login_as("user", "pass")`
- Locators are defined in one place (no duplication).

### Exercise — Run this code

```python
# exercise_13_page_object_model.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


# ── Base Page (shared by all pages) ──
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False


# ── Login Page ──
class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    HEADING = (By.TAG_NAME, "h2")

    def open(self):
        self.driver.get(self.URL)

    def login_as(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)

    def get_heading(self):
        return self.get_text(self.HEADING)

    def is_logged_in(self):
        return "You logged into a secure area!" in self.get_flash_message()


# ── Secure Area Page (after login) ──
class SecureAreaPage(BasePage):
    HEADING = (By.TAG_NAME, "h2")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    FLASH_MESSAGE = (By.ID, "flash")

    def get_heading(self):
        return self.get_text(self.HEADING)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_logged_out(self):
        return "You logged out of the secure area!" in self.get_text(self.FLASH_MESSAGE)


# ── Test ──
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # Test login
    login_page = LoginPage(driver)
    login_page.open()
    print(f"Page heading: '{login_page.get_heading()}'")

    login_page.login_as("tomsmith", "SuperSecretPassword!")
    print(f"Flash: '{login_page.get_flash_message()}'")
    assert login_page.is_logged_in()
    print("PASS: Login worked")

    # Test logout (using SecureAreaPage)
    secure_page = SecureAreaPage(driver)
    print(f"Secure area heading: '{secure_page.get_heading()}'")

    secure_page.click_logout()
    assert secure_page.is_logged_out()
    print("PASS: Logout worked")

finally:
    driver.quit()
```

---

## Chapter 14: Context Managers for Safe Cleanup

### Explanation
A context manager (`with` statement) ensures the browser is always closed, even if an error occurs. This is cleaner than `try/finally`.

### Exercise — Run this code

```python
# exercise_14_context_manager.py
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


@contextmanager
def firefox_browser(headless=False):
    """Context manager that auto-closes the browser."""
    from selenium.webdriver.firefox.options import Options
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    try:
        yield driver
    finally:
        driver.quit()
        print("Browser closed automatically.")


# ═══ Usage ═══
with firefox_browser() as driver:
    driver.get("https://the-internet.herokuapp.com")
    print(f"Title: '{driver.title}'")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Links on homepage: {len(links)}")

print("Browser was closed — even if an error happened above.")

# ═══ Headless mode ═══
with firefox_browser(headless=True) as driver:
    driver.get("https://www.google.com")
    print(f"\nHeadless mode — title: '{driver.title}'")

print("Headless browser closed automatically.")
```

---

## Chapter 15: Real-World Scraping Example

### Explanation
Combine everything: navigate, wait, extract data, handle pagination, save results.

### Exercise — Run this code

```python
# exercise_15_real_world_scraper.py
import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


def scrape_table_data(url: str) -> list[dict]:
    """Extract all rows from the sortable data tables page."""
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        # Wait for table
        table = wait.until(EC.presence_of_element_located((By.ID, "table1")))

        # Get headers
        header_cells = table.find_elements(By.CSS_SELECTOR, "thead th")
        headers = [th.text.strip() for th in header_cells]
        print(f"Headers: {headers}")

        # Get rows
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        print(f"Rows found: {len(rows)}")

        data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = {}
            for i, cell in enumerate(cells):
                if i < len(headers):
                    row_data[headers[i]] = cell.text.strip()
            data.append(row_data)

        return data

    finally:
        driver.quit()


def save_to_csv(data: list[dict], filename: str):
    with open(filename, "w", newline="") as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    print(f"Saved {len(data)} rows to '{filename}'")


# ═══ Run ═══
data = scrape_table_data("https://the-internet.herokuapp.com/tables")
for row in data[:3]:
    print(row)

save_to_csv(data, "scraped_data.csv")
```

---

## Appendix: Quick Reference

### Imports (copy-paste starter)

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, StaleElementReferenceException
)
from webdriver_manager.firefox import GeckoDriverManager
```

### Driver initialization

```python
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
```

### Common wait conditions

```python
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "myid")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".class")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//button"))))
wait.until(EC.text_to_be_present_in_element((By.ID, "x"), "text"))
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "spinner")))
wait.until(EC.alert_is_present())
wait.until(EC.number_of_windows_to_be(2))
```

### Common pitfalls

| Pitfall | Fix |
|---|---|
| `time.sleep()` everywhere | Replace with `WebDriverWait` |
| Absolute XPath (`/html/body/div[1]`) | Use relative XPath or CSS |
| Not closing the driver | Use `with` context manager or `try/finally` |
| Mixing implicit + explicit waits | Use only explicit waits |
| Stale element errors | Re-locate the element before reusing |
| NoSuchElementException on dynamic content | Add explicit wait before finding |
