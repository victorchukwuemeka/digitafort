from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser (Selenium Manager handles the driver automatically)
driver = webdriver.Chrome()  # or Firefox(), Edge(), Safari()

try:
    # Navigate to a website
    driver.get("https://www.example.com")
    
    # Wait for an element to load (up to 10 seconds)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "some-id"))
    )
    
    # Interact with elements
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium tutorial")
    search_box.submit()
    
    # Get page title
    print(driver.title)
    
finally:
    # Always close the browser
    driver.quit()