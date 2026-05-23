from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")

    #user by id
    username = driver.find_element(By.ID, "username")
    print(username.tag_name)
    password = driver.find_element(By.NAME, "password")
    print(password.tag_name)
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")


    username.send_keys("victor")
    password.send_keys("1234tkyky")

    print(button.is_enabled())
    print(button.is_displayed())

    print(username.get_attribute('value'))

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




"""

try:
    driver.get("https://the-internet.herokuapp.com/login")

    button  = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    print(button.text)

    icon = driver.find_element(By.CSS_SELECTOR, 'i.fa-sign-in')
    print(icon.get_attribute('class'))

    username = driver.find_element(By.CSS_SELECTOR, '#username')

    label = driver.find_element(By.CSS_SELECTOR, "label[for*='pass']")
    print(label.text)
    all_labels = driver.find_elements(By.CSS_SELECTOR, "label")
    print(f"Labels on page: {len(all_labels)}")
    for lbl in all_labels:
        print(f"  - '{lbl.text}'")
finally:
    driver.quit()

"""



"""
try:
    driver.get("https://the-internet.herokuapp.com/login")

    #user by id
    username = driver.find_element(By.ID, "username")
    print(username.tag_name)

    password = driver.find_element(By.NAME, "password")
    print(password.tag_name)

    css_class = driver.find_element(By.CLASS_NAME, "radius")
    print(css_class.text)

    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    count = 0
    for i in all_inputs:
        count+=1
    print(count)
finally:
    driver.quit()

"""





"""
driver = webdriver.Firefox()
driver.get("https://x.com/home")
assert "X" in driver.title
el = driver.find_element(By.NAME,"q")
el.clear()
el.send_keys("@viktr")
el.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

"""

#driver.close(
