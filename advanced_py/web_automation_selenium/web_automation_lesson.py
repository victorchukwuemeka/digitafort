"""
Web Automation — Capstone Exercise
====================================
This script demonstrates EVERYTHING from the course:
  1. Firefox setup with GeckoDriver
  2. Explicit waits
  3. All locator strategies
  4. Form interaction
  5. Dropdowns (Select class)
  6. Multiple windows
  7. JavaScript execution
  8. Hover (ActionChains)
  9. Alerts
  10. File upload
  11. Screenshots
  12. Page Object Model
  13. Error handling

Run it:  python web_automation_lesson.py
"""

import os
import time
import tempfile
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


SAVE_SCREENSHOTS = True


def log(msg: str):
    print(f"  ▶ {msg}")


def take_screenshot(driver, name: str):
    if not SAVE_SCREENSHOTS:
        return
    os.makedirs("screenshots", exist_ok=True)
    ts = datetime.now().strftime("%H%M%S")
    path = f"screenshots/{name}_{ts}.png"
    driver.save_screenshot(path)
    log(f"Screenshot saved: {path}")


def create_driver():
    options = Options()
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    return driver


# ═══════════════════════════════════════════════════
# 1. NAVIGATION BASICS
# ═══════════════════════════════════════════════════

def exercise_navigation(driver):
    print("\n═══ 1. NAVIGATION ═══")

    driver.get("https://the-internet.herokuapp.com")
    log(f"Opened: {driver.title}")

    driver.get("https://the-internet.herokuapp.com/login")
    log(f"Navigated to: {driver.title}")

    driver.back()
    log(f"Back button — title: '{driver.title}'")

    driver.forward()
    log(f"Forward button — title: '{driver.title}'")

    take_screenshot(driver, "01_navigation")


# ═══════════════════════════════════════════════════
# 2. LOCATORS + FORM INTERACTION + WAITS
# ═══════════════════════════════════════════════════

def exercise_login(driver):
    print("\n═══ 2. LOGIN (LOCATORS + WAITS + FORMS) ═══")

    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # By.ID
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")

    # By.NAME
    password = driver.find_element(By.NAME, "password")
    password.send_keys("SuperSecretPassword!")

    # By.CSS_SELECTOR
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()

    # Wait for success message
    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    log(f"Flash message: '{flash.text.strip()}'")

    assert "You logged into a secure area!" in flash.text
    log("PASS: Login successful")

    take_screenshot(driver, "02_login")


# ═══════════════════════════════════════════════════
# 3. DROPDOWNS (Select class)
# ═══════════════════════════════════════════════════

def exercise_dropdown(driver):
    print("\n═══ 3. DROPDOWN ═══")

    driver.get("https://the-internet.herokuapp.com/dropdown")

    select = Select(driver.find_element(By.ID, "dropdown"))

    log("Options:")
    for opt in select.options:
        log(f"     value='{opt.get_attribute('value')}' -> '{opt.text}'")

    select.select_by_visible_text("Option 2")
    chosen = select.first_selected_option.text
    log(f"Selected by text: '{chosen}'")
    assert chosen == "Option 2"

    select.select_by_value("1")
    chosen = select.first_selected_option.text
    log(f"Selected by value: '{chosen}'")
    assert chosen == "Option 1"

    log("PASS: All dropdown operations worked")


# ═══════════════════════════════════════════════════
# 4. MULTIPLE WINDOWS
# ═══════════════════════════════════════════════════

def exercise_windows(driver):
    print("\n═══ 4. MULTIPLE WINDOWS ═══")

    driver.get("https://the-internet.herokuapp.com/windows")
    main = driver.current_window_handle
    log(f"Main window: {main}")

    driver.find_element(By.LINK_TEXT, "Click Here").click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))

    for handle in driver.window_handles:
        if handle != main:
            driver.switch_to.window(handle)
            break

    text = driver.find_element(By.TAG_NAME, "h3").text
    log(f"New window text: '{text}'")
    assert "New Window" in text

    driver.close()
    driver.switch_to.window(main)
    log(f"Back to main: '{driver.title}'")

    log("PASS: Window switching worked")


# ═══════════════════════════════════════════════════
# 5. JAVASCRIPT EXECUTION
# ═══════════════════════════════════════════════════

def exercise_javascript(driver):
    print("\n═══ 5. JAVASCRIPT ═══")

    driver.get("https://the-internet.herokuapp.com/large")

    before = driver.execute_script("return window.scrollY;")
    log(f"Scroll position before: {before}px")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    after = driver.execute_script("return window.scrollY;")
    log(f"Scroll position after: {after}px")
    assert after > before

    title = driver.execute_script("return document.title;")
    log(f"Title via JS: '{title}'")

    table = driver.find_element(By.ID, "large-table")
    driver.execute_script("arguments[0].style.border = '3px solid red';", table)
    log("Table highlighted with red border")

    log("PASS: JavaScript execution works")


# ═══════════════════════════════════════════════════
# 6. HOVER (ActionChains)
# ═══════════════════════════════════════════════════

def exercise_hover(driver):
    print("\n═══ 6. HOVER (ActionChains) ═══")

    driver.get("https://the-internet.herokuapp.com/hovers")

    fig = driver.find_element(By.CSS_SELECTOR, ".figure")
    ActionChains(driver).move_to_element(fig).perform()
    time.sleep(0.5)

    caption = driver.find_element(By.CSS_SELECTOR, ".figcaption h5").text
    log(f"Caption after hover: '{caption}'")
    assert "user1" in caption

    log("PASS: Hover action works")


# ═══════════════════════════════════════════════════
# 7. ALERTS
# ═══════════════════════════════════════════════════

def exercise_alerts(driver):
    print("\n═══ 7. ALERTS ═══")

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS Alert
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    log(f"Alert text: '{alert.text}'")
    alert.accept()

    # JS Confirm — dismiss
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.dismiss()
    result = driver.find_element(By.ID, "result").text
    assert "Cancel" in result

    # JS Prompt
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.send_keys("Selenium!")
    alert.accept()
    result = driver.find_element(By.ID, "result").text
    assert "Selenium!" in result

    log("PASS: All alert types handled")


# ═══════════════════════════════════════════════════
# 8. FILE UPLOAD
# ═══════════════════════════════════════════════════

def exercise_upload(driver):
    print("\n═══ 8. FILE UPLOAD ═══")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                     prefix="selenium_", delete=False) as f:
        f.write("Hello from Selenium!")
        test_file = f.name

    try:
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.find_element(By.ID, "file-upload").send_keys(test_file)
        driver.find_element(By.ID, "file-submit").click()

        uploaded = driver.find_element(By.ID, "uploaded-files").text
        log(f"Uploaded file: '{uploaded}'")
        assert "selenium_" in uploaded
        log("PASS: File upload worked")
    finally:
        os.unlink(test_file)


# ═══════════════════════════════════════════════════
# 9. PAGE OBJECT MODEL (mini demo)
# ═══════════════════════════════════════════════════

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


class DynamicLoadingPage(BasePage):
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.ID, "finish")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    def click_start(self):
        self.click(self.START_BUTTON)

    def wait_for_finish(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.FINISH_TEXT)
        ).text


def exercise_pom(driver):
    print("\n═══ 9. PAGE OBJECT MODEL ═══")

    page = DynamicLoadingPage(driver)
    page.open()
    log("Opened dynamic loading page")

    page.click_start()
    text = page.wait_for_finish()
    log(f"Dynamic content loaded: '{text}'")
    assert "Hello World!" in text

    log("PASS: POM pattern works")


# ═══════════════════════════════════════════════════
# 10. DYNAMIC CONTENT + WAITS
# ═══════════════════════════════════════════════════

def exercise_dynamic_content(driver):
    print("\n═══ 10. DYNAMIC CONTENT ═══")

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    finish = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    log(f"Hidden element appeared: '{finish.text}'")
    assert finish.text == "Hello World!"

    log("PASS: Dynamic content wait works")


# ═══════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════

def main():
    print("=" * 55)
    print("  SELENIUM CAPSTONE — Firefox Edition")
    print("=" * 55)

    driver = create_driver()
    driver.maximize_window()

    try:
        exercise_navigation(driver)
        exercise_login(driver)
        exercise_dropdown(driver)
        exercise_windows(driver)
        exercise_javascript(driver)
        exercise_hover(driver)
        exercise_alerts(driver)
        exercise_upload(driver)
        exercise_pom(driver)
        exercise_dynamic_content(driver)

        print("\n" + "=" * 55)
        print("  ALL EXERCISES PASSED SUCCESSFULLY")
        print("=" * 55)

    except AssertionError as e:
        print(f"\n  ✗ FAILED: {e}")
        take_screenshot(driver, "FAILURE")
    except Exception as e:
        print(f"\n  ✗ ERROR: {e}")
        take_screenshot(driver, "ERROR")
    finally:
        print("\n  Closing browser in 3 seconds...")
        time.sleep(3)
        driver.quit()
        print("  Done.")


if __name__ == "__main__":
    main()
