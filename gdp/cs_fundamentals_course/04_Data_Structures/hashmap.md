# Hash Table Course

---

## Lesson 1 — What Is a Hash Table?

A hash table is a data structure that stores **key-value pairs** and lets you retrieve any value almost instantly by its key — regardless of how many items are stored.

Think of it like a filing cabinet where every drawer has a label. You go straight to the right drawer without searching through all of them.

> **Every language has one.** Python calls it a `dict`, JavaScript calls it an `object` or `Map`, Java calls it a `HashMap`. Same idea, different syntax.

```python
# key → value
person = {
    "name": "Ada",
    "age":  12,
    "city": "London"
}

print(person["age"])   # → 12  (instant lookup)
```

---

## Lesson 2 — How It Works Inside

Internally, a hash table is just an **array** (a list of slots). When you store a key like `"name"`, a **hash function** converts that key into a number — the index where the value will be stored.

```
Keys  →  Hash Function  →  Index  →  Value
"name"  →  h("name") = 2  →  slot 2  →  "Ada"
"age"   →  h("age")  = 0  →  slot 0  →  12
"city"  →  h("city") = 4  →  slot 4  →  "London"
```

The hash function always produces the **same index for the same key**. That's what makes lookups instant — you run the same function and jump straight to the right slot.

### What about collisions?

Sometimes two different keys hash to the same slot. That's called a **collision**. Hash tables handle these automatically (using chaining or open addressing) — as a user, you never need to think about it.

---

## Lesson 3 — Core Operations

All four core operations run in **O(1)** average time — the same speed whether you have 10 items or 10 million.

| Operation | Syntax (Python)            | Time    |
|-----------|----------------------------|---------|
| Insert    | `d["key"] = value`         | O(1)    |
| Lookup    | `d["key"]`                 | O(1)    |
| Update    | `d["key"] = new_value`     | O(1)    |
| Delete    | `del d["key"]`             | O(1)    |

```python
person = {"name": "Ada", "age": 12}

# lookup
print(person["age"])       # → 12

# update
person["age"] = 13

# insert
person["job"] = "coder"

# delete
del person["name"]

print(person)  # → {"age": 13, "job": "coder"}
```

> **Why does this matter?** A plain list requires scanning every element to find a match — O(n). Hash tables are dramatically faster for key-based access.

---

## Lesson 4 — When to Use a Hash Table

Use a hash table when:

- You need **fast lookups by a named key** (not by position)
- You want to **count frequencies** — e.g. how many times each word appears
- You want to **group or bucket data** by a category
- You need to **cache results** to avoid repeating expensive work
- You want to **check membership** quickly (is this item in the set?)

### Real-world examples

**Counting word frequency**
```python
text = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}

for word in text:
    counts[word] = counts.get(word, 0) + 1

print(counts)  # → {"apple": 3, "banana": 2, "cherry": 1}
```

**Caching expensive results**
```python
cache = {}

def get_user(user_id):
    if user_id in cache:
        return cache[user_id]          # instant — already computed
    result = expensive_db_query(user_id)
    cache[user_id] = result
    return result
```

**Grouping data**
```python
students = [("Alice", "Math"), ("Bob", "Science"), ("Carol", "Math")]
by_subject = {}

for name, subject in students:
    by_subject.setdefault(subject, []).append(name)

# → {"Math": ["Alice", "Carol"], "Science": ["Bob"]}
```

### When *not* to use one

- You need items in **sorted order** → use a sorted list or tree
- You need to access items **by position** (index 0, 1, 2…) → use an array
- Your keys aren't hashable (e.g. lists) → use a different structure

---

## Quick Reference

```
Hash Table Cheat Sheet
─────────────────────────────────────────────
Create       d = {}  /  d = dict()
Insert       d["key"] = value
Lookup       d["key"]             → value
Safe lookup  d.get("key", default)
Update       d["key"] = new_value
Delete       del d["key"]
Check key    "key" in d           → True/False
All keys     d.keys()
All values   d.values()
All pairs    d.items()
─────────────────────────────────────────────
Average time for all operations: O(1)
Worst case (rare collisions):    O(n)
```

---

## Quiz — Test Yourself

**Q1.** You have a list of 1 million names and need to check if "Alice" is in it. Which is faster?

- A) Scanning the list one by one
- B) Looking "Alice" up in a hash table

> **B** — Hash table lookup is O(1). Scanning the list is O(n), which could mean checking all 1 million entries.

---

**Q2.** What does a hash function do?

- A) Encrypts the key for security
- B) Converts a key into an array index
- C) Sorts the keys alphabetically

> **B** — The hash function maps a key to a slot number in the underlying array.

---

**Q3.** You want to count how many times each letter appears in a string. Which data structure fits best?

- A) A sorted list
- B) A hash table (dictionary)
- C) A queue

>  **B** — Hash tables are the natural choice for counting frequencies by key.

---

**Q4.** Which of these is a limitation of hash tables?

- A) They can only store numbers
- B) They don't support deletion
- C) They don't maintain insertion order (in most implementations)

> **C** — Traditional hash tables give no ordering guarantees. (Note: Python's `dict` preserves insertion order since Python 3.7, but that's a language-specific feature.)

---

*End of course. You now understand what hash tables are, how they work, their core operations, and when to reach for them.*