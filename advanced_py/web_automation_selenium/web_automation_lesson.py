"""
Selenium Web Automation Lesson
Target Site: https://the-internet.herokuapp.com/login

This script demonstrates:
1. Automatic driver management with webdriver-manager.
2. Using Explicit Waits (WebDriverWait) for stability.
3. Finding elements by ID and CSS Selector.
4. Handling login forms and verifying success.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def run_lesson():
    # 1. Setup Chrome Options (Optional: e.g., --headless)
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Uncomment to run without a visible browser

    # 2. Initialize Driver with Automatic Download
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("Starting Lesson: Navigating to Demo Site...")
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

        # 3. Use Explicit Wait to ensure the element is ready
        wait = WebDriverWait(driver, 10)
        
        print("Locating Username and Password fields...")
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # 4. Interaction
        print("Entering credentials...")
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        
        print("Clicking login...")
        login_button.click()

        # 5. Verification
        # Wait for the flash message to appear
        flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        print("\n--- Results ---")
        if "You logged into a secure area!" in flash_message.text:
            print("SUCCESS: Login test passed.")
        else:
            print("FAILURE: Login failed or message changed.")
        print(f"Final Page Title: {driver.title}")

    except Exception as e:
        print(f"An error occurred during the lesson: {e}")

    finally:
        # Keep the browser open for 3 seconds so students can see the result
        import time
        time.sleep(3)
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    run_lesson()
