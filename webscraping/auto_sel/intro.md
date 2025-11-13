## What Selenium is and why use it

**Selenium** is an open-source framework that automates web browsers. It allows you to programmatically control a browser (Chrome, Firefox, Safari, etc.) to perform actions like clicking buttons, filling forms, navigating pages, and extracting data.

**Why use Selenium:**
- **Testing web applications** - Selenium is primarily designed for automated testing of web apps across different browsers
- **Handling dynamic content** - It executes JavaScript and waits for pages to fully load, unlike simple HTTP requests
- **Complex interactions** - Can simulate real user behavior like scrolling, hovering, and multi-step workflows
- **Authentication** - Can handle login sessions, cookies, and authentication flows
- **Cross-browser compatibility** - Tests can run on multiple browsers to ensure consistency

## Browser automation vs web scraping

**Browser automation** is the broader concept of programmatically controlling a browser to perform tasks. It includes testing, form submission, automated workflows, and yes, data extraction.

**Web scraping** specifically refers to extracting data from websites. You can scrape using:
- **Simple HTTP requests** (like `requests` in Python) - Fast and lightweight, but only gets the initial HTML
- **Browser automation** (like Selenium) - Slower and resource-heavy, but handles JavaScript-rendered content

Think of it this way: all browser automation for data extraction is web scraping, but not all web scraping requires browser automation.

## Dynamic vs static websites

**Static websites** serve pre-rendered HTML. When you request a page, the server sends complete HTML with all content already in it. You can scrape these with simple HTTP requests because everything is already in the source code.

**Dynamic websites** load content using JavaScript after the initial page loads. When you view the page source, you might see placeholder divs or script tags, but not the actual data. The content appears through:
- AJAX requests fetching data from APIs
- JavaScript frameworks (React, Vue, Angular) rendering content client-side
- Infinite scrolling or lazy loading

**Examples:**
- Static: Traditional blogs, documentation sites, simple portfolios
- Dynamic: Social media feeds, single-page applications, real-time dashboards

For dynamic sites, Selenium is often necessary because it executes the JavaScript and waits for content to appear, whereas a simple HTTP request would only capture the empty initial HTML.