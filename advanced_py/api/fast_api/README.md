# FastAPI — Comprehensive Course

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints.

## 1. Installation

```bash
pip install fastapi uvicorn
```

## 2. Hello World

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Run: `uvicorn main:app --reload`

- Docs: `http://127.0.0.1:8000/docs` (Swagger UI)
- Alternative: `http://127.0.0.1:8000/redoc`

## 3. Path Parameters

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):        # Type validation automatically
    return {"item_id": item_id}
```

FastAPI validates the type and returns a 422 error if invalid.

### Path Parameter with Validation

```python
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(ge=1, description="Item ID")):
    ...
```

## 4. Query Parameters

```python
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]
```

### Query with Validation

```python
from fastapi import Query

@app.get("/items/")
def list_items(
    q: str = Query(None, max_length=50, description="Search query"),
    price_min: float = Query(None, ge=0),
):
    ...
```

## 5. Request Body with Pydantic

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    tax: float | None = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

## 6. Response Model (Data Filtering)

```python
class UserPublic(BaseModel):
    username: str
    email: str

class UserPrivate(UserPublic):
    password: str

@app.post("/users/", response_model=UserPublic)
def create_user(user: UserPrivate):
    return user  # password will be filtered out
```

## 7. Status Codes

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    ...

@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int):
    ...
```

## 8. Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]
```

## 9. Path, Query, and Body Combined

```python
@app.post("/users/{user_id}/orders")
def create_order(
    user_id: int,                          # path
    order: Order,                          # body (JSON)
    discount: str | None = None,           # query
):
    ...
```

## 10. Enum Parameters

```python
from enum import Enum

class Status(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"

@app.get("/orders/{status}")
def get_by_status(status: Status):
    return {"status": status.value}
```

## 11. File Upload

```python
@app.post("/upload/")
async def upload_file(file: bytes | None = None):
    if file:
        return {"size": len(file)}
    return {"message": "No file"}
```

For larger files, use `UploadFile` from `fastapi.UploadFile`.

## 12. Dependency Injection

```python
from fastapi import Depends

def common_params(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def list_items(params: dict = Depends(common_params)):
    return params
```

## 13. Authentication (Simple)

```python
from fastapi import Header, HTTPException

@app.get("/protected/")
def protected_route(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth")
    return {"message": "Authenticated"}
```

## 14. CORS (Cross-Origin Resource Sharing)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 15. Testing with `httpx` & `pytest`

```python
from fastapi.testclient import TestClient

def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

## 16. Project Structure Best Practices

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app instance
│   ├── models.py         # Pydantic models
│   ├── database.py       # DB connection
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   ├── dependencies.py   # Shared deps
│   └── schemas.py        # Request/response schemas
├── tests/
├── requirements.txt
└── .env
```

## Key Takeaways
- FastAPI uses Python type hints for validation, serialization, and docs
- Pydantic models define request/response shapes
- Automatic interactive docs at `/docs` and `/redoc`
- Built-in validation with `Path`, `Query`, `Field`
- Response models filter output data automatically
- Dependency injection promotes clean, reusable code
