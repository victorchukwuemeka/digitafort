# Practical: Inventory + Checkout Engine

## Goal
Design a small but realistic system using composition, validation, and clean class APIs.

## Requirements
Implement the following classes:

### 1. `Product`
- Attributes: `sku`, `name`, `price`
- Validation: `price` must be >= 0
- `__repr__` should show sku + price

### 2. `Inventory`
- Holds stock as a mapping of `sku -> quantity`
- Methods: `add_stock(sku, qty)`, `remove_stock(sku, qty)`, `available(sku)`
- Raise `ValueError` if removing more than available

### 3. `CartItem`
- Attributes: `product`, `qty`
- Validation: qty >= 1

### 4. `Cart`
- Holds `CartItem` objects
- Methods: `add(product, qty)`, `remove(sku)`, `total()`

### 5. `Checkout`
- Takes `Inventory` + `Cart`
- Method: `place_order()`
    - Verifies stock
    - Deducts stock
    - Returns a receipt dict: `{"items": [...], "total": ...}`

## Stretch Goals
1. Add `discounts` with a strategy object.
2. Use `@dataclass` for `Product` and `CartItem`.
3. Add `__eq__` to compare products by `sku`.

## Suggested File
Create a file named `inventory.py` and implement the classes. Add a short manual test at the bottom.
