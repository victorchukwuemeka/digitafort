"""
Classwork: Consuming APIs with Python
API Used: JSONPlaceholder (https://jsonplaceholder.typicode.com)
Instructions: Complete the functions below.
Run with: pytest classwork.py -v
"""
import requests


def get_all_users() -> list[dict]:
    """Fetch all users from /users endpoint. Return the list of users."""
    # TODO: GET https://jsonplaceholder.typicode.com/users
    pass


def get_user_posts(user_id: int) -> list[dict]:
    """Fetch all posts for a given userId using query params.
    Return the list of posts."""
    # TODO: GET https://jsonplaceholder.typicode.com/posts?userId={user_id}
    pass


def create_post(title: str, body: str, user_id: int) -> dict:
    """Create a new post using POST. Return the created post dict."""
    # TODO: POST https://jsonplaceholder.typicode.com/posts with JSON body
    pass


def get_post_titles_longer_than(posts: list[dict], min_length: int) -> list[str]:
    """From a list of posts, return titles that exceed min_length characters."""
    # TODO: Filter and return titles
    pass


def get_user_email_domains(users: list[dict]) -> list[str]:
    """Extract unique email domains (e.g. '@biz' from 'John@biz') from users."""
    # TODO: Parse emails and return sorted unique domains
    pass


def safe_get_post(post_id: int) -> dict | None:
    """Return the post if found (200), None if 404, raise on other errors."""
    # TODO: Handle status codes properly
    pass


# ============================================================
# Tests (run with pytest)
# ============================================================

def test_get_all_users():
    users = get_all_users()
    assert isinstance(users, list)
    assert len(users) == 10
    assert "name" in users[0]
    assert "email" in users[0]


def test_get_user_posts():
    posts = get_user_posts(1)
    assert isinstance(posts, list)
    for p in posts:
        assert p["userId"] == 1


def test_create_post():
    post = create_post("Test Title", "Test Body", 1)
    assert post["title"] == "Test Title"
    assert post["body"] == "Test Body"
    assert "id" in post


def test_get_post_titles_longer_than():
    posts = [{"title": "ab"}, {"title": "abcde"}, {"title": "a"}]
    result = get_post_titles_longer_than(posts, 2)
    assert result == ["abcde"]


def test_get_user_email_domains():
    users = [
        {"email": "john@biz"},
        {"email": "jane@biz"},
        {"email": "doe@com"},
    ]
    result = get_user_email_domains(users)
    assert result == ["@biz", "@com"]


def test_safe_get_post_found():
    post = safe_get_post(1)
    assert post is not None
    assert "title" in post


def test_safe_get_post_not_found():
    result = safe_get_post(99999)
    assert result is None
