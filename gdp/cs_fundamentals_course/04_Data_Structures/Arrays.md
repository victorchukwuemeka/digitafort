# Lesson 1: Arrays

An **array** is an ordered collection stored in contiguous memory. In Python, the built-in `list` behaves like a **dynamic array** (it grows and shrinks automatically).

## Learning Goals
- Understand what arrays are and why contiguous memory matters.
- Use indexing to read and update elements.
- Know the cost of common operations.
- Practice small, real-world tasks with arrays.

## Key Properties
- **Ordered:** Items keep their position (index).
- **Indexed:** You access items by number (0-based).
- **Contiguous memory:** Elements sit next to each other in memory.
- **Dynamic size (Python lists):** Size changes as you append or delete.

## Core Operations (with Python list)
- **Access by index:** `arr[i]` (fast)
- **Update by index:** `arr[i] = value`
- **Append:** `arr.append(x)` (amortized fast)
- **Insert in middle:** `arr.insert(i, x)` (slow)
- **Delete by index:** `arr.pop(i)` or `del arr[i]` (slow)
- **Search by value:** `x in arr` or `arr.index(x)` (slow)

## Time Complexity (Big‑O)
| Operation | Average Time |
|---|---|
| Access by index | `O(1)` |
| Update by index | `O(1)` |
| Search by value | `O(n)` |
| Append at end | `O(1)` amortized |
| Insert in middle | `O(n)` |
| Delete in middle | `O(n)` |

## Tiny Example
```python
numbers = [10, 20, 30, 40]
print(numbers[2])   # 30
numbers[2] = 35
numbers.append(50)
print(numbers)      # [10, 20, 35, 40, 50]
```

## Common Mistakes
- **Index out of range:** `arr[len(arr)]` is invalid.
- **Confusing negative indexes:** `arr[-1]` is the last element.
- **Assuming insert/delete is always fast:** It can be slow for big lists.

## Practice Tasks (Beginner)
1. Create a list of 5 friends and print the first and last names.
2. Insert a new item at index 2.
3. Remove the third item and print the list.
4. Find the index of a value (or print “not found”).
5. Loop through the list and print each item with its index.

## Quick Summary
- Arrays are **fast for indexing**, **slow for middle insert/delete**.
- Python `list` is a **dynamic array** that grows automatically.
- Use arrays when you need ordered data and fast random access.
