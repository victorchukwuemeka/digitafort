# Web Automation with Selenium & Python: Course Guide

## Introduction
Web automation allows you to simulate human interaction with a web browser. It is widely used for automated testing, data scraping, and automating repetitive web tasks.

## Course Curriculum

### 1. Fundamentals of Selenium
*   **What is Selenium?** An open-source suite of tools for automating web browsers.
*   **Architecture:** Script -> WebDriver -> Browser.
*   **Environment Setup:**
    *   Python installation.
    *   `pip install selenium webdriver-manager`.

### 2. Locating Elements (The Core Skill)
To interact with a page, you must first find the elements.
*   **By ID:** `By.ID` (Fastest and most reliable).
*   **By Name:** `By.NAME`.
*   **By CSS Selector:** `By.CSS_SELECTOR` (Powerful and flexible).
*   **By XPath:** `By.XPATH` (Best for complex structures).
*   **By Link Text:** `By.LINK_TEXT` or `By.PARTIAL_LINK_TEXT`.

### 3. Interacting with Elements
*   `click()`: Clicking buttons or links.
*   `send_keys()`: Typing into input fields.
*   `clear()`: Clearing text from an input.
*   `text`: Retrieving text from an element.
*   `get_attribute()`: Getting attribute values (like `href` or `src`).

### 4. Synchronization (Handling Dynamic Content)
The biggest challenge in automation is timing.
*   **Implicit Waits:** Global wait for elements to appear.
*   **Explicit Waits (Best Practice):** Wait for a specific condition (e.g., `element_to_be_clickable`).
*   **Fluent Waits:** Polling at intervals.

### 5. Advanced Interactions
*   Handling Dropdowns (`Select` class).
*   Alerts, Frames, and Windows.
*   ActionChains: Hovering, Drag & Drop.

### 6. Design Patterns
*   **Page Object Model (POM):** Separating the page structure from the test logic to improve maintainability.

---

## Teaching Today: Practical Exercise
The accompanying `web_automation_lesson.py` covers:
1.  Automatic Driver Management.
2.  Navigation and Window management.
3.  Explicit Waits (the professional way to wait).
4.  Form interaction and verification.
