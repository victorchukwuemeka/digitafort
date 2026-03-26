# Module 1: Foundations: Web, Django & Authorization

## Lesson 2: Web Fundamentals & Django Core

In this lesson, we'll dive into the fundamental concepts that underpin almost all modern web applications. We'll explore the client-server model, the HTTP protocol, RESTful principles, and then introduce Django as a powerful framework for building web applications based on these principles.

---

### The Client-Server Model

The internet primarily operates on a **client-server model**. This is a distributed application architecture where tasks are partitioned between:

*   **Clients:** Request information or services. This is typically a web browser (like Chrome, Firefox) on your computer or mobile device, but it could also be a mobile app, a desktop application, or even another server making requests.
*   **Servers:** Provide information or services in response to client requests. A server is essentially a powerful computer that stores files, runs applications, and delivers data.

**How it Works:**
1.  A **client** sends a request (e.g., to load a webpage, submit a form, or fetch data) to a **server**.
2.  The **server** processes the request, retrieves or generates the necessary data, and sends a response back to the client.
3.  The **client** then interprets and displays this response to the user.

This model allows for a clear separation of concerns, with clients focusing on user interaction and presentation, and servers handling business logic, data storage, and security.

---

### HTTP/HTTPS: The Language of the Web

**HTTP (Hypertext Transfer Protocol)** is the primary protocol used for transferring information on the World Wide Web. It's a stateless protocol, meaning each request from a client to the server is treated as an independent transaction, without any memory of previous requests.

Key aspects of HTTP:

*   **Requests:** Sent by clients and consist of:
    *   **Method (Verb):** Indicates the desired action (e.g., `GET` to retrieve data, `POST` to send data, `PUT` to update, `DELETE` to remove).
    *   **URL (Uniform Resource Locator):** Specifies the resource the client wants to interact with.
    *   **Headers:** Provide metadata about the request (e.g., `User-Agent`, `Accept`, `Content-Type`).
    *   **Body (Optional):** Contains the actual data being sent (e.g., form data for a `POST` request).
*   **Responses:** Sent by servers and consist of:
    *   **Status Code:** A three-digit number indicating the request's outcome (e.g., `200 OK`, `404 Not Found`, `500 Internal Server Error`).
    *   **Headers:** Metadata about the response (e.g., `Content-Type`, `Set-Cookie`).
    *   **Body (Optional):** The actual data being returned (e.g., HTML, JSON, an image).

**HTTPS (Hypertext Transfer Protocol Secure)** is simply the secure version of HTTP. It uses **SSL/TLS (Secure Sockets Layer/Transport Layer Security)** to encrypt the communication between the client and server, protecting data from eavesdropping and tampering. Always use HTTPS for any production web application!

---

### REST APIs: Structured Communication

**REST (Representational State Transfer)** is an architectural style for designing networked applications. It's not a protocol, but a set of guidelines for how clients and servers should communicate. APIs (Application Programming Interfaces) that adhere to REST principles are called **RESTful APIs**.

Key REST principles:

1.  **Client-Server Separation:** As discussed above, the client and server are decoupled.
2.  **Statelessness:** Each request from client to server must contain all the information needed to understand the request. The server should not store any client context between requests.
3.  **Cacheability:** Responses should explicitly or implicitly define themselves as cacheable to prevent clients from reusing stale or inappropriate data.
4.  **Uniform Interface:** Simplifies and decouples the architecture, allowing each part to evolve independently. This includes:
    *   **Resource Identification in Requests:** Individual resources are identified in requests, e.g., `/users/123`, `/posts/new`.
    *   **Resource Manipulation Through Representations:** Clients manipulate resources using representations (e.g., JSON, XML) in the request body.
    *   **Self-Descriptive Messages:** Each message includes enough information to describe how to process the message.
    *   **Hypermedia as the Engine of Application State (HATEOAS):** Resources include links to related resources, guiding the client on available actions. (Often ignored in practical REST API design).
5.  **Layered System:** A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way.

**Example RESTful Interaction:**

*   `GET /api/posts` -> Retrieve a list of all posts.
*   `POST /api/posts` -> Create a new post (data in request body).
*   `GET /api/posts/123` -> Retrieve details of post with ID 123.
*   `PUT /api/posts/123` -> Update post with ID 123 (full data in body).
*   `PATCH /api/posts/123` -> Partially update post with ID 123 (partial data in body).
*   `DELETE /api/posts/123` -> Delete post with ID 123.

---

### Introduction to Django: A Web Framework

**Django** is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

Django follows the **MVT (Model-View-Template)** architectural pattern, which is a variation of MVC (Model-View-Controller) commonly used in other frameworks.

*   **Model:** This is the data layer. It defines your data structure, typically mapping to a database table. In Django, models are Python classes that inherit from `django.db.models.Model`. They handle data storage, retrieval, and validation.
    *   *Example:* A `Post` model would define fields like `title`, `content`, `author`.

*   **View:** This is the business logic layer. In Django, a "view" is a Python function or class that receives an HTTP request, processes it, interacts with the model to fetch or save data, and returns an HTTP response (often by rendering a template).
    *   *Example:* A view function `post_list(request)` would fetch all posts from the `Post` model and prepare them for display.

*   **Template:** This is the presentation layer. It defines how data is displayed to the user. Django's templating language allows you to embed Python-like logic within HTML to dynamically generate web pages.
    *   *Example:* An HTML file `post_list.html` would iterate over the posts received from the view and display their titles and content.

**How Django handles a request (the MVT flow):**

1.  **Request arrives:** A user's browser sends an HTTP request to your Django application.
2.  **`urls.py` (URL Dispatcher):** Django's URL dispatcher (defined in your project's `urls.py`) matches the incoming URL to a specific view function or class.
3.  **View receives request:** The matched view receives the `HttpRequest` object.
4.  **View processes logic:** The view performs its business logic:
    *   It might interact with **Models** to query or save data to the database.
    *   It might perform calculations or validations.
5.  **View renders Template (optional):** If the view needs to display data to the user via an HTML page, it passes data to a **Template**.
6.  **Response sent:** The view constructs an `HttpResponse` object (e.g., rendered HTML, JSON data, a redirect) and sends it back to the user's browser.

---

### Setting up a Basic Django Project (Recap from `mini.md`)

Let's quickly recap the initial steps for setting up a Django project, as we'll be using this as our practical foundation throughout the course.

1.  **Install Django:**
    ```bash
    pip install Django
    ```
2.  **Create a Project:**
    ```bash
    django-admin startproject auth_project
    cd auth_project
    ```
3.  **Create an App:**
    ```bash
    python manage.py startapp blog
    ```
4.  **Register the App:** Add `'blog'` to `INSTALLED_APPS` in `auth_project/settings.py`.
5.  **Define a Model:** In `blog/models.py`, create your `Post` model.
    ```python
    # blog/models.py
    from django.db import models
    from django.contrib.auth.models import User

    class Post(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

        def __str__(self):
            return self.title
    ```
6.  **Make and Apply Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7.  **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```
8.  **Configure URLs:** Include your app's URLs in the main `auth_project/urls.py` and create a `blog/urls.py`.
9.  **Create Basic Views and Templates:** (We will do this more thoroughly in the practical section).

---

### Conclusion

Understanding the client-server model, HTTP/HTTPS, and RESTful principles provides the essential context for building web applications. Django, with its MVT architecture, offers a robust and efficient way to implement these concepts. In the next lesson, we'll dive deep into Django's authentication and authorization system, which is crucial for building secure applications.

---
**Further Reading (Optional):**
*   [Mozilla Developer Network: HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
*   [REST API Tutorial](https://www.restapitutorial.com/)
*   [Django Documentation: What is Django?](https://docs.djangoproject.com/en/stable/intro/overview/)
