from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://x.com/home")
assert "X" in driver.title
el = driver.find_element(By.NAME,"q")
el.clear()
el.send_keys("@viktr")
el.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

#driver.close()
