# Lesson 1: Arrays

An **array** is an ordered collection stored in contiguous memory. In Python, the built-in `list` behaves like a **dynamic array** — it grows and shrinks automatically so you don't have to manage memory yourself.

---

## Learning Goals

By the end of this lesson you should be able to:

- Explain what an array is and why contiguous memory matters.
- Use indexing to read, update, and slice elements.
- Know the time cost of every common operation and *why*.
- Spot and fix the most common array mistakes.
- Complete the practice tasks without looking anything up.

---

## What Is Contiguous Memory?

When you create an array, all its elements are stored **side by side** in memory:

```
Index:    0     1     2     3
Value:   [10]  [20]  [30]  [40]
Address: 100   104   108   112
```

Because the positions are evenly spaced, the computer can jump straight to any element with a single calculation:

```
address of arr[i] = base_address + (i × element_size)
```

This is why reading or updating any element takes **O(1)** — constant time, no matter how big the array is.

---

## Key Properties

| Property | What it means |
|---|---|
| **Ordered** | Items keep their position (index). Order is guaranteed. |
| **0-based indexing** | The first element is at index `0`, not `1`. |
| **Contiguous memory** | Elements sit next to each other — enables O(1) access. |
| **Dynamic size (Python)** | Python `list` resizes automatically when you append or delete. |

---

## Core Operations

```python
arr = [10, 20, 30, 40]

# Read by index — O(1)
print(arr[2])         # 30

# Update by index — O(1)
arr[2] = 35
print(arr)            # [10, 20, 35, 40]

# Append to end — O(1) amortized
arr.append(50)
print(arr)            # [10, 20, 35, 40, 50]

# Insert in middle — O(n): everything after shifts right
arr.insert(2, 99)
print(arr)            # [10, 20, 99, 35, 40, 50]

# Delete by index — O(n): everything after shifts left
arr.pop(2)
print(arr)            # [10, 20, 35, 40, 50]

# Search by value — O(n): scans from left until found
print(35 in arr)      # True
print(arr.index(35))  # 2

# Slicing — O(k) where k is the slice length
print(arr[1:4])       # [20, 35, 40]

# Negative indexing — counts from the end
print(arr[-1])        # 50  (last element)
print(arr[-2])        # 40  (second to last)
```

---

## Time Complexity

| Operation | Time | Why |
|---|---|---|
| Access by index | O(1) | Direct memory calculation |
| Update by index | O(1) | Direct memory write |
| Append at end | O(1) amortized | Usually just writes to pre-allocated space |
| Insert in middle | O(n) | All elements after the point must shift right |
| Delete in middle | O(n) | All elements after the point must shift left |
| Search by value | O(n) | May need to scan every element |
| Slice `[i:j]` | O(k) | Copies k elements into a new list |

> **Amortized O(1) for append:** Python pre-allocates extra space when the list grows. Most appends are O(1). Occasionally the list doubles its capacity — that one operation is O(n) — but averaged across many appends, the cost per operation is still O(1).

---

## Negative Indexing — Visual

Negative indexes count backwards from the end. This is useful when you don't know the length.

```
arr =  [10,  20,  30,  40,  50]
index:   0    1    2    3    4
neg:    -5   -4   -3   -2   -1

arr[-1]  → 50   (last)
arr[-2]  → 40   (second to last)
arr[-5]  → 10   (same as arr[0])
```

---

## Common Mistakes

**1. Index out of range**
```python
arr = [10, 20, 30]
print(arr[3])   # IndexError — valid indexes are 0, 1, 2
print(arr[-4])  # IndexError — valid negative indexes are -1, -2, -3
```

**2. Modifying a list while looping over it**
```python
# BAD — skips elements
arr = [1, 2, 3, 4]
for x in arr:
    if x % 2 == 0:
        arr.remove(x)

# GOOD — loop over a copy
for x in arr[:]:
    if x % 2 == 0:
        arr.remove(x)
```

**3. Assuming insert/delete is always fast**
```python
arr = list(range(1_000_000))
arr.insert(0, -1)   # O(n) — shifts 1 million elements. This is slow.
arr.pop(0)          # O(n) — same problem.
```
If you frequently insert or delete at the front, use `collections.deque` instead.

**4. Confusing `=` (reference) with `copy()`**
```python
a = [1, 2, 3]
b = a           # b points to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4]  — a changed too!

b = a.copy()    # b is now an independent copy
b.append(5)
print(a)        # [1, 2, 3, 4]  — a is unchanged
```

---

## Useful Built-in Functions

```python
arr = [3, 1, 4, 1, 5, 9]

len(arr)          # 6       — number of elements
min(arr)          # 1       — smallest value
max(arr)          # 9       — largest value
sum(arr)          # 23      — total
sorted(arr)       # [1, 1, 3, 4, 5, 9]  — returns new sorted list
arr.sort()        # sorts arr in place (modifies original)
arr.reverse()     # reverses arr in place
arr.count(1)      # 2       — how many times 1 appears
```

---

## Practice Tasks

Work through these in order. Don't skip ahead.

**Task 1 — Create and access**
Create a list of 5 city names. Print the first, last, and middle city using indexing.

**Task 2 — Update and insert**
Take the list from Task 1. Change the second city to a different name. Then insert a new city at index 2.

**Task 3 — Delete and search**
Remove the third city from the list. Then check if a specific city name is in the list and print "Found" or "Not found".

**Task 4 — Loop with index**
Loop through the list using `enumerate` and print each item in this format:
```
1. Lagos
2. Accra
3. Nairobi
```

**Task 5 — Solve a problem**
Write a function `find_max(arr)` that returns the largest number in a list **without using `max()`**. Use a loop.

**Task 6 — Think about cost**
You have a list of 1 million numbers. Which of these is fast and which is slow? Explain why.
```python
arr[500_000]         # read middle element
arr.append(99)       # add to end
arr.insert(0, 99)    # add to front
arr.pop(0)           # remove from front
```

---

## Quick Summary

- Arrays store elements in **contiguous memory** — that is what makes O(1) access possible.
- **Indexing and updating** are always fast: O(1).
- **Insert and delete in the middle** are always slow: O(n) because elements must shift.
- Python `list` is a **dynamic array** — it handles resizing for you.
- Use an array when you need **ordered data and fast random access**.
- If you need fast inserts/deletes at both ends, use `collections.deque` instead.

---

## What's Next

**Lesson 2: Strings** — strings are essentially read-only character arrays. You will see many of the same indexing patterns, plus new operations like slicing, splitting, and searching for patterns.