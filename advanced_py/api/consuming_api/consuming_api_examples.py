"""
Comprehensive Examples: Consuming APIs in Python
"""
import os
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ============================================================
# 1. Basic GET Request
# ============================================================
def basic_get():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"GET {url}")
    print(f"Status: {response.status_code}")
    print(f"Title: {data['title']}\n")


# ============================================================
# 2. Query Parameters
# ============================================================
def query_parameters():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    posts = response.json()
    print(f"GET {url} with params={params}")
    print(f"Found {len(posts)} posts for user 1\n")


# ============================================================
# 3. POST Request (Creating Data)
# ============================================================
def create_resource():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    created = response.json()
    print(f"POST {url}")
    print(f"Status: {response.status_code} (201 = Created)")
    print(f"Created ID: {created['id']}\n")


# ============================================================
# 4. PUT & PATCH Requests
# ============================================================
def update_resource():
    base = "https://jsonplaceholder.typicode.com/posts/1"

    # PUT — full replacement
    put_resp = requests.put(base, json={"title": "updated", "body": "new", "userId": 1}, timeout=10)
    put_resp.raise_for_status()
    print(f"PUT: {put_resp.json()['title']}")

    # PATCH — partial update
    patch_resp = requests.patch(base, json={"title": "patched"}, timeout=10)
    patch_resp.raise_for_status()
    print(f"PATCH: {patch_resp.json()['title']}\n")


# ============================================================
# 5. DELETE Request
# ============================================================
def delete_resource():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url, timeout=10)
    print(f"DELETE {url} — Status: {response.status_code} (204 = No Content)\n")


# ============================================================
# 6. Headers & Authentication
# ============================================================
def custom_headers():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {
        "Accept": "application/json",
        "User-Agent": "MyAPIClient/1.0",
    }
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Headers sent: {headers}")
    print(f"Response Headers: {dict(response.headers)}\n")


# ============================================================
# 7. Sessions (Connection Reuse)
# ============================================================
def use_session():
    with requests.Session() as session:
        session.headers.update({"Accept": "application/json"})
        for post_id in range(1, 4):
            resp = session.get(
                f"https://jsonplaceholder.typicode.com/posts/{post_id}",
                timeout=10,
            )
            resp.raise_for_status()
            print(f"Post {post_id}: {resp.json()['title']}")
    print()


# ============================================================
# 8. Retry Logic & Rate Limiting
# ============================================================
def retry_on_failure():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        resp = session.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        resp.raise_for_status()
        print(f"Retry strategy — Status: {resp.status_code}\n")
    except requests.exceptions.RetryError as e:
        print(f"Failed after retries: {e}\n")


# ============================================================
# 9. Error Handling
# ============================================================
def error_handling_demo():
    scenarios = [
        ("Timeout", "https://httpbin.org/delay/10"),
        ("Client Error", "https://httpbin.org/status/404"),
        ("Server Error", "https://httpbin.org/status/500"),
    ]

    for label, url in scenarios:
        try:
            resp = requests.get(url, timeout=3)
            resp.raise_for_status()
        except requests.exceptions.Timeout:
            print(f"{label}: Request timed out")
        except requests.exceptions.HTTPError as e:
            print(f"{label}: HTTP {e.response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{label}: {e}")
    print()


# ============================================================
# 10. Pagination
# ============================================================
def fetch_all_paginated():
    base_url = "https://jsonplaceholder.typicode.com/posts"
    all_posts = []
    page = 1
    per_page = 10

    while True:
        resp = requests.get(base_url, params={"_page": page, "_limit": per_page}, timeout=10)
        if resp.status_code != 200 or not resp.json():
            break
        all_posts.extend(resp.json())
        page += 1

    print(f"Fetched {len(all_posts)} posts via pagination\n")


# ============================================================
# 11. Async HTTP with httpx
# ============================================================
def async_example():
    try:
        import httpx
        import asyncio

        async def fetch():
            async with httpx.AsyncClient() as client:
                tasks = [
                    client.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10),
                    client.get("https://jsonplaceholder.typicode.com/posts/2", timeout=10),
                ]
                results = await asyncio.gather(*tasks)
                for r in results:
                    print(f"Async GET: {r.json()['title']}")

        asyncio.run(fetch())
        print()
    except ImportError:
        print("httpx not installed. Install with: pip install httpx\n")


# ============================================================
# 12. Environment Variables for Secrets
# ============================================================
def use_env_var():
    api_key = os.getenv("API_KEY", "demo-key")
    print(f"Using API Key: {api_key[:4]}... (from env or default)\n")


# ============================================================
# Main Runner
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("COMPREHENSIVE API CONSUMING EXAMPLES")
    print("=" * 60)

    basic_get()
    query_parameters()
    create_resource()
    update_resource()
    delete_resource()
    custom_headers()
    use_session()
    retry_on_failure()
    error_handling_demo()
    fetch_all_paginated()
    async_example()
    use_env_var()
