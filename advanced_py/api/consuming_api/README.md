# Consuming APIs — Comprehensive Course

## 1. What is an API?
API (Application Programming Interface) allows two applications to communicate. Web APIs use HTTP to exchange data, typically in JSON format.

## 2. HTTP Methods
| Method  | Purpose        | Example                  |
|---------|----------------|--------------------------|
| GET     | Read data      | Get a list of users      |
| POST    | Create data    | Create a new user        |
| PUT     | Replace data   | Replace a user entirely  |
| PATCH   | Partial update | Update user's email      |
| DELETE  | Remove data    | Delete a user            |

## 3. HTTP Status Codes
- `200 OK` — Success
- `201 Created` — Resource created
- `204 No Content` — Success, no body
- `400 Bad Request` — Client error
- `401 Unauthorized` — Authentication needed
- `403 Forbidden` — No permission
- `404 Not Found` — Resource doesn't exist
- `429 Too Many Requests` — Rate limited
- `500 Internal Server Error` — Server error

## 4. The `requests` Library
### Installation
```bash
pip install requests
```

### Basic GET Request
```python
import requests
response = requests.get("https://api.example.com/users")
print(response.status_code)
print(response.json())        # Parse JSON
print(response.text)          # Raw text
print(response.headers)       # Response headers
```

### Query Parameters
```python
params = {"page": 2, "limit": 10}
response = requests.get("https://api.example.com/users", params=params)
```

### POST Request with JSON Body
```python
data = {"name": "John", "email": "john@example.com"}
response = requests.post("https://api.example.com/users", json=data)
```

### Headers & Authentication
```python
headers = {"Authorization": "Bearer YOUR_TOKEN", "Accept": "application/json"}
response = requests.get("https://api.example.com/protected", headers=headers)
```

### API Key Authentication
```python
response = requests.get("https://api.example.com/data", params={"api_key": "YOUR_KEY"})
```

### Error Handling
```python
try:
    response = requests.get("https://api.example.com/users", timeout=10)
    response.raise_for_status()  # Raises for 4xx/5xx
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### Sessions (Connection Reuse)
```python
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer TOKEN"})
    resp1 = session.get("https://api.example.com/users")
    resp2 = session.get("https://api.example.com/posts")
```

## 5. Async HTTP with `httpx`
```python
import httpx
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/users")
        return response.json()

results = asyncio.run(fetch_data())
```

## 6. Rate Limiting & Retries
```python
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503])
session.mount("https://", HTTPAdapter(max_retries=retries))

response = session.get("https://api.example.com/users")
```

## 7. File Uploads
```python
files = {"file": open("photo.jpg", "rb")}
response = requests.post("https://api.example.com/upload", files=files)
```

## 8. Downloading Large Files (Streaming)
```python
response = requests.get("https://example.com/large.zip", stream=True)
with open("output.zip", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## 9. Working with Paginated APIs
```python
def fetch_all_pages(base_url, params=None):
    all_data = []
    page = 1
    while True:
        params = params or {}
        params["page"] = page
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data["results"]:
            break
        all_data.extend(data["results"])
        page += 1
    return all_data
```

## 10. Best Practices
- Always use `timeout` — prevent hanging requests
- Use `raise_for_status()` — catch HTTP errors early
- Use sessions for multiple requests to the same host
- Respect `Retry-After` headers on 429 responses
- Store secrets (API keys, tokens) in environment variables
- Use `.env` files and `python-dotenv` for local secrets
