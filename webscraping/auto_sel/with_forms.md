**Working with Forms**

Forms include input fields, dropdowns, checkboxes, radio buttons, and submit buttons.

**Common Form Actions:**

- **Text inputs:** `.send_keys("text")` and `.clear()`
- **Dropdowns:** Use `Select` class
- **Checkboxes/Radio buttons:** `.click()` to select
- **Submit:** `.submit()` or click submit button

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://example.com/registration")

# Text input
name_field = driver.find_element(By.ID, "name")
name_field.send_keys("John Doe")

# Email input
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("john@example.com")

# Dropdown
country_dropdown = driver.find_element(By.ID, "country")
select = Select(country_dropdown)
select.select_by_visible_text("United States")
# Or: select.select_by_value("us")
# Or: select.select_by_index(1)

# Checkbox
terms_checkbox = driver.find_element(By.ID, "terms")
if not terms_checkbox.is_selected():
    terms_checkbox.click()

# Radio button
gender_radio = driver.find_element(By.ID, "male")
gender_radio.click()

# Submit form
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

driver.quit()
```