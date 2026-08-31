# Consuming APIs — Comprehensive Course

## Table of Contents

1. [What is an API?](#1-what-is-an-api)
2. [How HTTP Actually Works](#2-how-http-actually-works)
3. [HTTP Methods](#3-http-methods)
4. [HTTP Status Codes](#4-http-status-codes)
5. [The `requests` Library](#5-the-requests-library)
6. [Query Parameters](#6-query-parameters)
7. [POST Requests & Sending Data](#7-post-requests--sending-data)
8. [Headers & Authentication](#8-headers--authentication)
9. [Error Handling](#9-error-handling)
10. [Sessions — Connection Reuse](#10-sessions--connection-reuse)
11. [Retries & Exponential Backoff](#11-retries--exponential-backoff)
12. [File Uploads](#12-file-uploads)
13. [Streaming Downloads](#13-streaming-downloads)
14. [Pagination](#14-pagination)
15. [Async HTTP with `httpx`](#15-async-http-with-httpx)
16. [Security & Best Practices](#16-security--best-practices)
17. [Complete Runnable Example](#17-complete-runnable-example)

---

## 1. What is an API?

An **API** (Application Programming Interface) is a contract between two pieces of software. It defines: "if you send me **this**, I'll respond with **that**."

Think of it like a **waiter in a restaurant**. You (the client) don't walk into the kitchen and grab food. You tell the waiter what you want, the waiter takes it to the kitchen (the server), and brings back your meal. The waiter is the API — the interface between you and the kitchen.

In web development, APIs almost always work over **HTTP**. Your Python script sends an HTTP request to a server, and the server sends back an HTTP response — usually in **JSON** format:

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(data["name"])  # "The Octocat"
```

Here's what happened:
1. `requests.get()` opened a connection to `api.github.com`
2. Sent an HTTP GET request to `/users/octocat`
3. GitHub's server looked up that user in its database
4. Sent back a JSON response with the user's data
5. `response.json()` parsed that JSON into a Python dictionary

---

## 2. How HTTP Actually Works

Every API call follows the same pattern:

**Request** (your script sends):
```
GET /users/octocat HTTP/1.1
Host: api.github.com
Accept: application/json
Authorization: Bearer ghp_xxxxxxxxxxxx
```

**Response** (server sends back):
```
HTTP/1.1 200 OK
Content-Type: application/json

{"login": "octocat", "name": "The Octocat", "public_repos": 8}
```

Three parts of every request:
- **Method** — what you want to do (GET, POST, PUT, DELETE)
- **Path** — which resource you're targeting (`/users/octocat`)
- **Headers** — metadata about the request (auth tokens, content type, etc.)

Three parts of every response:
- **Status code** — did it work? (200 = yes, 404 = not found, 500 = server broke)
- **Headers** — metadata about the response (content type, cache info, rate limits)
- **Body** — the actual data (usually JSON)

---

## 3. HTTP Methods

Each method has a specific meaning. Using the right one makes your code self-documenting and ensures the server behaves correctly:

| Method | Purpose | Has Body? | Idempotent? | Example |
|--------|---------|-----------|-------------|---------|
| **GET** | Read data | No | Yes | Fetch a list of users |
| **POST** | Create data | Yes | No | Create a new user |
| **PUT** | Replace an entire resource | Yes | Yes | Replace a user's profile |
| **PATCH** | Partial update | Yes | No | Update only a user's email |
| **DELETE** | Remove a resource | No | Yes | Delete a user |

**What does "idempotent" mean?** If you send the same request twice, you get the same result. GET is idempotent — asking for `/users/1` twice gives you the same user. POST is NOT — sending `POST /users` twice creates two users.

**PUT vs PATCH — this trips everyone up:**

```python
# PUT — replace EVERYTHING. Missing fields become null/default.
requests.put("/users/123", json={"name": "Alice", "email": "alice@new.com"})
# Now the user has NO phone number, NO address — they weren't in the PUT body

# PATCH — update ONLY what you send. Other fields stay unchanged.
requests.patch("/users/123", json={"email": "alice@new.com"})
# Name, phone, address — all still there
```

Always prefer PATCH for updates unless you're intentionally replacing the entire resource.

---

## 4. HTTP Status Codes

Status codes tell you what happened. They're grouped into five categories:

**2xx — Success:**
- `200 OK` — everything worked
- `201 Created` — a new resource was created (check the `Location` header for its URL)
- `204 No Content` — success, but there's nothing to send back (common for DELETE)

**4xx — Client Error (you messed up):**
- `400 Bad Request` — your request is malformed (wrong JSON, missing required fields)
- `401 Unauthorized` — you're not authenticated (no token, or expired/invalid token)
- `403 Forbidden` — you're authenticated but not allowed to do this (regular user trying admin action)
- `404 Not Found` — the resource doesn't exist at that URL
- `409 Conflict` — duplicate (e.g., trying to create a user with an email that already exists)
- `422 Unprocessable Entity` — your JSON is valid but the data doesn't make sense (negative price, etc.)
- `429 Too Many Requests` — you're rate limited. Check the `Retry-After` header

**5xx — Server Error (they messed up):**
- `500 Internal Server Error` — something broke on their end
- `502 Bad Gateway` — the server got an invalid response from upstream
- `503 Service Unavailable` — the server is overloaded or down for maintenance

**The most important rule:** never ignore status codes. A `200` response with error details in the body is still a success — the error is in your logic, not the HTTP layer. A `500` means don't bother parsing the body.

---

## 5. The `requests` Library

`requests` is the standard HTTP client in Python. It handles all the low-level networking — DNS, TCP connections, TLS encryption, HTTP parsing — behind a clean API.

```bash
pip install requests
```

### Making a Request

```python
import requests

response = requests.get("https://api.example.com/users")
```

### The Response Object

```python
response.status_code    # 200
response.ok             # True (status < 400)
response.json()         # parsed dict — {"users": [...]}
response.text           # raw string — '{"users": [...]}'
response.headers        # dict — {"Content-Type": "application/json", ...}
response.content        # raw bytes (for binary data like images)
response.url            # the final URL (after redirects)
response.history        # list of redirects that happened
response.elapsed        # timedelta — how long the request took
```

**`response.json()` vs `json.loads(response.text)`** — they do the same thing, but `.json()` also:
- Checks the `Content-Type` header
- Handles character encoding automatically
- Raises a clear error if the body isn't valid JSON

Always prefer `.json()`.

### Timeout — Never Skip This

```python
# BAD — hangs forever if the server doesn't respond
resp = requests.get("https://api.example.com/slow")

# GOOD — fails after 10 seconds
resp = requests.get("https://api.example.com/slow", timeout=10)
```

Without a timeout, your script blocks indefinitely. Even if the server is down, your script will wait forever for a response that never comes. **Always set a timeout.** Even 30 seconds is better than nothing.

---

## 6. Query Parameters

Query parameters filter or paginate results. They appear after `?` in the URL:

```
https://api.example.com/users?page=2&limit=10&sort=name
```

**Never build query strings manually.** The `requests` library handles URL encoding for you:

```python
# WRONG — what if the search query contains spaces or special characters?
resp = requests.get(f"https://api.example.com/search?q={query}&page={page}")

# RIGHT — requests encodes it properly
resp = requests.get("https://api.example.com/search", params={"q": query, "page": page})
```

If `query = "hello world"`, the wrong approach sends `q=hello world` (broken — space in URL). The right approach sends `q=hello+world` or `q=hello%20world` (correct).

### Multiple Parameters

```python
params = {
    "page": 2,
    "limit": 10,
    "sort": "created_at",
    "order": "desc",
    "status": "active",
}
resp = requests.get("https://api.example.com/users", params=params)
# Requests builds: /users?page=2&limit=10&sort=created_at&order=desc&status=active
```

---

## 7. POST Requests & Sending Data

POST creates new resources. You send data in the request body:

```python
payload = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}
resp = requests.post("https://api.example.com/users", json=payload)
```

**`json=` vs `data=`:**
- `json=payload` — sets `Content-Type: application/json` and serializes the dict to JSON
- `data=payload` — sends as form data (like an HTML form submission)

```python
# JSON (what APIs expect)
requests.post(url, json={"name": "Alice"})

# Form data (for file uploads or old-style APIs)
requests.post(url, data={"name": "Alice"})
```

Almost every modern API expects JSON. Use `json=` unless the API docs say otherwise.

### PUT and PATCH work the same way

```python
# PUT — full replacement
requests.put(f"{BASE_URL}/users/123", json={"name": "Alice", "email": "a@b.com"})

# PATCH — partial update
requests.patch(f"{BASE_URL}/users/123", json={"email": "new@b.com"})
```

### DELETE

```python
resp = requests.delete(f"{BASE_URL}/users/123")
# Usually returns 204 No Content on success
```

---

## 8. Headers & Authentication

Headers carry metadata about the request. The most common ones:

```python
headers = {
    "Authorization": "Bearer YOUR_JWT_TOKEN",    # auth token
    "Content-Type": "application/json",          # what you're sending
    "Accept": "application/json",                # what you want back
    "User-Agent": "MyApp/1.0",                   # identify your client
}
resp = requests.get("https://api.example.com/me", headers=headers)
```

### Bearer Token Auth (JWT)

The most common pattern for APIs. You get a token after login, send it with every request:

```python
# After logging in
login_resp = requests.post(f"{BASE_URL}/auth/login", json={
    "username": "alice", "password": "secret123"
})
token = login_resp.json()["access_token"]

# Use the token for protected endpoints
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get(f"{BASE_URL}/users/me", headers=headers)
```

When the token expires, you get a `401 Unauthorized` and need to re-login or refresh the token.

### API Key Auth

Some services use API keys instead of tokens. Two patterns:

```python
# In query params (common for weather, news APIs)
resp = requests.get("https://api.weather.com/forecast", params={"apikey": "YOUR_KEY"})

# In headers (more secure — key doesn't appear in URLs/logs)
resp = requests.get("https://api.stripe.com/charges", headers={"Authorization": "sk_live_YOUR_KEY"})
```

---

## 9. Error Handling

**The #1 mistake beginners make:** no error handling at all.

```python
# BAD — crashes if the server returns an error page (HTML, not JSON)
resp = requests.get(url)
data = resp.json()
```

The right approach handles three categories of failures:

```python
import requests

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()   # raises HTTPError for 4xx/5xx
    data = resp.json()

except requests.exceptions.Timeout:
    print("Server took too long to respond")

except requests.exceptions.ConnectionError:
    print("Could not connect — server might be down")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
    print(f"Details: {e.response.text}")

except requests.exceptions.JSONDecodeError:
    print("Response was not valid JSON")

except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")
```

**The key line is `raise_for_status()`.** Without it, a `500 Internal Server Error` silently succeeds — `resp.json()` returns whatever garbage the error page contains, and your code proceeds with bad data.

**Why `timeout=10`?** Without it, your script hangs forever. If the server is slow or dead, you're stuck. Timeout ensures your code fails fast and can handle the failure.

---

## 10. Sessions — Connection Reuse

Every `requests.get()` creates a new TCP connection, does a DNS lookup, and performs a TLS handshake. If you're making 10 requests to the same host, that's 10 separate handshakes — wasteful.

**Sessions** reuse the underlying connection:

```python
# WITHOUT session — 3 separate connections
requests.get("https://api.example.com/users")
requests.get("https://api.example.com/posts")
requests.get("https://api.example.com/comments")

# WITH session — 1 connection, reused 3 times
with requests.Session() as session:
    session.get("https://api.example.com/users")
    session.get("https://api.example.com/posts")
    session.get("https://api.example.com/comments")
```

Sessions also **persist headers and cookies** across requests:

```python
with requests.Session() as session:
    # Set headers once — applies to ALL requests in this session
    session.headers.update({
        "Authorization": "Bearer TOKEN",
        "Accept": "application/json",
    })

    resp1 = session.get("https://api.example.com/users")
    resp2 = session.get("https://api.example.com/posts")
    # Both requests automatically include the Authorization header
```

**When to use sessions:** Always, when making 2+ requests to the same host.

---

## 11. Retries & Exponential Backoff

Networks fail. Servers go down. Rate limits kick in. A robust client retries failed requests — but not immediately. **Exponential backoff** means waiting longer between each retry:

```
Retry 1: wait 0.5 seconds
Retry 2: wait 1 second
Retry 3: wait 2 seconds
```

This gives the server time to recover. Retrying immediately (no backoff) makes outages worse — you're hammering a struggling server with more requests.

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry_strategy = Retry(
    total=3,                              # max 3 retries
    backoff_factor=0.5,                   # wait 0.5s, 1s, 2s
    status_forcelist=[429, 500, 502, 503, 504],  # retry on these status codes
    allowed_methods=["GET"],              # only retry GET (not POST)
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)

resp = session.get("https://api.example.com/data")
```

**Why only retry GET?** POST/PUT/PATCH might not be **idempotent** — if the server received your request but the response was lost, retrying creates a duplicate (two users, two charges, etc.). Only retry operations that are safe to repeat.

**Check `Retry-After` on 429:** When rate limited, the server tells you how long to wait:

```python
resp = requests.get(url)
if resp.status_code == 429:
    retry_after = int(resp.headers.get("Retry-After", 60))
    time.sleep(retry_after)
    resp = requests.get(url)  # retry after waiting
```

---

## 12. File Uploads

Upload files with multipart form data:

```python
# Simple upload
files = {"file": open("photo.jpg", "rb")}
resp = requests.post("https://api.example.com/upload", files=files)
```

**With metadata:**

```python
resp = requests.post(
    "https://api.example.com/upload",
    files={"file": ("photo.jpg", open("photo.jpg", "rb"), "image/jpeg")},
    data={"description": "My vacation photo", "tags": "travel"},
)
```

The `files` dict format is: `{field_name: (filename, file_object, content_type)}`.

**Always use binary mode (`"rb"`)** — text mode corrupts images and binary files.

**In-memory files** for testing or small data:

```python
from io import BytesIO

fake_csv = BytesIO(b"name,age\nAlice,30\nBob,25")
resp = requests.post(
    "https://api.example.com/import",
    files={"file": ("data.csv", fake_csv, "text/csv")},
)
```

---

## 13. Streaming Downloads

Without streaming, `requests` downloads the entire file into memory before giving you the response. A 2GB file → 2GB of RAM used.

With `stream=True`, it downloads in chunks — constant memory usage regardless of file size:

```python
# WITHOUT streaming — loads entire file into memory
resp = requests.get("https://example.com/large.zip")
with open("large.zip", "wb") as f:
    f.write(resp.content)  # 2GB in memory!

# WITH streaming — constant memory usage
resp = requests.get("https://example.com/large.zip", stream=True)
with open("large.zip", "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        f.write(chunk)  # only 8KB at a time
```

**With progress tracking:**

```python
resp = requests.get("https://example.com/large.zip", stream=True)
total = int(resp.headers.get("content-length", 0))
downloaded = 0

with open("output.zip", "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        f.write(chunk)
        downloaded += len(chunk)
        print(f"\r{downloaded}/{total} bytes ({downloaded*100//total}%)", end="")
```

---

## 14. Pagination

Real APIs don't return all records at once. They return a "page" of results with metadata about total count:

```json
{
    "items": [...],
    "total": 1247,
    "page": 2,
    "per_page": 20,
    "pages": 63
}
```

**Offset-based pagination** (page numbers):

```python
def fetch_all_pages(base_url, params=None):
    all_data = []
    page = 1
    while True:
        p = params or {}
        p["page"] = page
        resp = requests.get(base_url, params=p, timeout=10)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data.get("results"):
            break
        all_data.extend(data["results"])
        page += 1
    return all_data
```

**Cursor-based pagination** (for large datasets):

```python
def fetch_all_cursor(base_url):
    all_data = []
    cursor = None
    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        resp = requests.get(base_url, params=params, timeout=10)
        data = resp.json()
        all_data.extend(data["items"])
        cursor = data.get("next_cursor")
        if not cursor:
            break
    return all_data
```

Cursor-based is better for large datasets — offset-based gets slower as page numbers increase (the database skips N rows).

---

## 15. Async HTTP with `httpx`

When you need to make many requests concurrently, `httpx` is the answer. It fires all requests at once and waits for them to complete — much faster than sequential requests.

```python
import asyncio
import httpx

async def fetch_all():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]

    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for resp in responses:
            print(resp.json()["title"])

asyncio.run(fetch_all())
```

**Why is this faster?**

```
Sequential:  req1 (1s) → req2 (1s) → req3 (1s)  = 3 seconds total
Async:       req1 ─┐
           req2 ─┼→ all complete ≈ 1 second total
           req3 ─┘
```

**Connection pooling** — `httpx.AsyncClient` reuses connections automatically. For high-volume scenarios:

```python
limits = httpx.Limits(max_connections=100, max_keepalive_connections=20)
async with httpx.AsyncClient(limits=limits) as client:
    ...
```

---

## 16. Security & Best Practices

| Practice | Why It Matters |
|----------|---------------|
| Always set `timeout` | Prevents your script from hanging forever on a dead server |
| Use `raise_for_status()` | Catches HTTP errors before you process bad data |
| Use sessions for multiple requests | Reuses connections — faster and more efficient |
| Retry with exponential backoff | Handles transient failures gracefully |
| Stream large downloads | Prevents memory exhaustion |
| Never hardcode API keys | If you commit secrets to git, they're exposed forever |
| Use `.env` files + `python-dotenv` | Load secrets from files that are gitignored |
| Check `Retry-After` headers | Respect rate limits instead of brute-forcing |
| Validate response schemas | Don't trust external APIs — verify the data shape |

### Using `.env` Files

```bash
# Install python-dotenv
pip install python-dotenv
```

```python
# .env file (NEVER commit this to git)
API_KEY=sk_live_1234567890abcdef
API_SECRET=super_secret_value
```

```python
# Python code
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env into environment variables

api_key = os.getenv("API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}
```

Add `.env` to your `.gitignore` so it never gets committed.

---

## 17. Complete Runnable Example

See **`consuming_api_examples.py`** for a single file demonstrating every pattern above with runnable code. Run it with:

```bash
python consuming_api_examples.py
```

See **`classwork.py`** for practice exercises with tests. Complete the functions and run:

```bash
pytest classwork.py -v
```

---

## Key Takeaways

- **Always use `timeout` and `raise_for_status()`** — the two most important lines in any API client
- **Sessions** reuse connections — essential when making 2+ requests to the same host
- **Retry with backoff** — networks are unreliable, plan for failures gracefully
- **Async (`httpx`)** for concurrent requests — orders of magnitude faster for batch operations
- **Stream large files** — `stream=True` keeps memory usage constant regardless of file size
- **Never hardcode secrets** — use environment variables and `.env` files
- **PUT replaces everything, PATCH updates what you send** — mixing them up causes data loss
