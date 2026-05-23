"""
Comprehensive FastAPI Examples — Building APIs in Python

Run: uvicorn fast_api_examples:app --reload
Docs: http://127.0.0.1:8000/docs
"""
from datetime import date, datetime
from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Path, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Comprehensive FastAPI Course",
    description="A complete example covering FastAPI features",
    version="1.0.0",
)


# ============================================================
# In-Memory Database
# ============================================================
items_db: dict[int, "Item"] = {}
users_db: dict[int, "User"] = {}
next_item_id = 1
next_user_id = 1


# ============================================================
# Pydantic Models (Data Validation)
# ============================================================
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    price: float = Field(..., gt=0, description="Item price")
    is_offer: bool = False
    tax: Optional[float] = Field(None, ge=0, le=100)


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    full_name: Optional[str] = None
    age: int = Field(..., ge=0, le=150)


class UserPublic(BaseModel):
    """Response model — excludes sensitive fields."""
    username: str
    full_name: Optional[str] = None
    age: int


class OrderStatus(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(BaseModel):
    item_id: int
    quantity: int = Field(..., ge=1, le=100)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)


# ============================================================
# Root Endpoint
# ============================================================
@app.get("/", tags=["General"])
def read_root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the FastAPI Course API",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


# ============================================================
# Path Parameters
# ============================================================
@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int = Path(..., ge=1, description="The ID of the item")):
    """Get an item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


# ============================================================
# Query Parameters
# ============================================================
@app.get("/items/", tags=["Items"])
def list_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max items to return"),
    min_price: Optional[float] = Query(None, ge=0),
):
    """List items with pagination and filtering."""
    items = list(items_db.values())
    if min_price is not None:
        items = [i for i in items if i.price >= min_price]
    return items[skip : skip + limit]


# ============================================================
# POST — Create Resource
# ============================================================
@app.post("/items/", status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: Item):
    """Create a new item."""
    global next_item_id
    item_data = item.model_dump()
    item_data["id"] = next_item_id
    items_db[next_item_id] = item
    next_item_id += 1
    return item_data


# ============================================================
# PUT — Full Update
# ============================================================
@app.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: Item):
    """Replace an item entirely."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"id": item_id, **item.model_dump()}


# ============================================================
# PATCH — Partial Update
# ============================================================
@app.patch("/items/{item_id}", tags=["Items"])
def patch_item(item_id: int, updates: dict):
    """Partially update an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    allowed = {"name", "price", "is_offer", "tax"}
    current = items_db[item_id]
    for key, value in updates.items():
        if key in allowed:
            setattr(current, key, value)
    return {"id": item_id, **current.model_dump()}


# ============================================================
# DELETE
# ============================================================
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]


# ============================================================
# Request Body + Path + Query Params
# ============================================================
@app.post("/users/{user_id}/orders", tags=["Orders"])
def create_order(
    user_id: int,
    order: Order,
    discount_code: Optional[str] = Query(None, max_length=20),
):
    """Create an order for a user (mix of path, body, query)."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    if order.item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "user_id": user_id,
        "order": order.model_dump(),
        "discount_applied": discount_code is not None,
    }


# ============================================================
# Response Model (Filtering Output)
# ============================================================
@app.post("/users/", status_code=201, response_model=UserPublic, tags=["Users"])
def create_user(user: User):
    """Create a user — returns public fields only."""
    global next_user_id
    users_db[next_user_id] = user
    next_user_id += 1
    return user


@app.get("/users/{user_id}", response_model=UserPublic, tags=["Users"])
def get_user(user_id: int):
    """Get a user — sensitive fields excluded."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


# ============================================================
# Enum Parameter
# ============================================================
@app.get("/orders/status/{status}", tags=["Orders"])
def get_orders_by_status(status: OrderStatus):
    """Get all orders with a given status (demonstrates enum params)."""
    return {"status": status.value, "message": f"Filtering by {status.value}"}


# ============================================================
# File Upload (via form)
# ============================================================
@app.post("/upload/", tags=["Files"])
async def upload_file(file: bytes = None):
    """Upload a file as bytes."""
    if file is None:
        return {"message": "No file uploaded"}
    return {"file_size": len(file)}


# ============================================================
# Custom Status Code & Headers
# ============================================================
@app.get("/custom-response/", tags=["Advanced"])
def custom_response():
    from fastapi.responses import JSONResponse

    content = {"message": "Custom response with headers"}
    return JSONResponse(
        content=content,
        status_code=201,
        headers={"X-Custom-Header": "custom-value"},
    )


# ============================================================
# Health Check
# ============================================================
@app.get("/health/", tags=["General"])
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


# ============================================================
# Run Directly
# ============================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fast_api_examples:app", host="0.0.0.0", port=8000, reload=True)
