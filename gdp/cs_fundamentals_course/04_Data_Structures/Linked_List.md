# Lesson 2: Linked Lists

A **linked list** is a chain of nodes where each node stores a value and a reference (pointer) to the next node. Unlike arrays, nodes do not need to sit next to each other in memory.

---

## Learning Goals

By the end of this lesson you should be able to:

- Explain how linked lists differ from arrays in memory layout.
- Identify and describe the three types of linked lists.
- Build a singly linked list using a `Node` class.
- Insert and delete nodes at common positions.
- Trace pointer changes without losing the list.
- Complete the practice tasks and assignment without looking anything up.

---

## Visual Model

```
Array:  [10][20][30][40]           (contiguous)
List:    10 -> 20 -> 30 -> 40 -> null  (scattered)
```

Each box is a **node**:

```
[value | next]
```

---

## Three Types of Linked Lists

### 1. Singly Linked List
Each node has a value and a single pointer to the **next** node. Traversal is one-directional (head to tail).

```
head -> 10 -> 20 -> 30 -> null
```

- Simple and memory-efficient.
- Cannot traverse backwards.

### 2. Doubly Linked List
Each node has a value, a pointer to the **next** node, and a pointer to the **previous** node. Traversal is bi-directional.

```
null <- 10 <-> 20 <-> 30 -> null
```

- Can traverse forward and backward.
- Uses more memory (extra pointer per node).
- Easier to delete a node when you have a reference to it (no need to track `prev` separately).

### 3. Circular Linked List
Similar to a singly or doubly linked list, but the **last node points back to the head** instead of `null`. This creates a loop.

```
head -> 10 -> 20 -> 30 -> (back to head)
```

- Useful for round-robin scheduling, circular buffers, or any problem that cycles through elements repeatedly.
- Must be careful when traversing — use a stop condition (e.g., stop when you return to head) to avoid infinite loops.

---

## Key Properties

| Property | What it means |
|---|---|
| **Non-contiguous memory** | Nodes can live anywhere in memory. |
| **No random access** | You must traverse from the head to reach a position. |
| **Fast insert/delete at head** | Change just a couple of pointers. |
| **Dynamic size** | Grows and shrinks without resizing. |

---

## Comparison of List Types

| Feature | Singly | Doubly | Circular |
|---|---|---|---|
| Traversal direction | Forward only | Forward & backward | Forward (loops) |
| Memory per node | 1 pointer | 2 pointers | 1 pointer (or 2 if doubly circular) |
| Delete node (given reference) | O(n) — need `prev` | O(1) — has `prev` pointer | O(n) |
| Common use case | Stacks, simple lists | Deques, browser history | Schedulers, buffers |

---

## Core Operations (Singly Linked)

| Operation | Time | Why |
|---|---|---|
| Insert at head | O(1) | Just rewire head pointer |
| Insert at tail | O(n) | Must traverse to end |
| Delete at head | O(1) | Move head pointer |
| Delete by value | O(n) | Must find the node first |
| Search | O(n) | Linear traversal |
| Traverse | O(n) | Visit each node |

---

## Python Implementations

### 1. Singly Linked List

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        self.head = Node(value, self.head)

    def insert_tail(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.value == value:
                prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def contains(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out


# --- Usage ---
sl = SinglyLinkedList()
sl.insert_tail(10)
sl.insert_tail(20)
sl.insert_tail(30)
sl.insert_head(5)
print(sl.to_list())          # [5, 10, 20, 30]
sl.delete_value(20)
print(sl.to_list())          # [5, 10, 30]
print(sl.contains(10))       # True
print(sl.contains(99))       # False
```

---

### 2. Doubly Linked List

Each node carries both a `next` and a `prev` pointer, enabling backward traversal and O(1) deletion when you already hold a reference to the node.

```python
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_tail(self, value):
        node = DoublyNode(value)
        if self.tail is None:
            self.head = self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete_value(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                if cur.prev:
                    cur.prev.next = cur.next   # bypass cur going forward
                else:
                    self.head = cur.next       # cur was the head
                if cur.next:
                    cur.next.prev = cur.prev   # bypass cur going backward
                else:
                    self.tail = cur.prev       # cur was the tail
                return True
            cur = cur.next
        return False

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def to_list_reversed(self):
        out = []
        cur = self.tail
        while cur:
            out.append(cur.value)
            cur = cur.prev
        return out


# --- Usage ---
dl = DoublyLinkedList()
dl.insert_tail(10)
dl.insert_tail(20)
dl.insert_tail(30)
dl.insert_head(5)
print(dl.to_list())           # [5, 10, 20, 30]
print(dl.to_list_reversed())  # [30, 20, 10, 5]
dl.delete_value(20)
print(dl.to_list())           # [5, 10, 30]
```

---

### 3. Circular Linked List

The last node's `next` points back to `head` instead of `null`. Always guard traversal with a step counter or a check against the head to avoid an infinite loop.

```python
class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = CircularNode(value)
        if self.head is None:
            self.head = node
            node.next = self.head          # point back to itself
            return
        cur = self.head
        while cur.next is not self.head:   # find the last node
            cur = cur.next
        cur.next = node
        node.next = self.head              # new tail points back to head

    def delete_value(self, value):
        if self.head is None:
            return False
        # Special case: deleting the head
        if self.head.value == value:
            if self.head.next is self.head:  # only one node
                self.head = None
                return True
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = self.head.next       # last node skips old head
            self.head = self.head.next
            return True
        prev = self.head
        cur = self.head.next
        while cur is not self.head:
            if cur.value == value:
                prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def to_list(self, steps):
        """Print `steps` nodes to avoid infinite loop."""
        out = []
        cur = self.head
        for _ in range(steps):
            if cur is None:
                break
            out.append(cur.value)
            cur = cur.next
        return out


# --- Usage ---
cl = CircularLinkedList()
cl.insert(10)
cl.insert(20)
cl.insert(30)
print(cl.to_list(3))    # [10, 20, 30]       — one full pass
print(cl.to_list(6))    # [10, 20, 30, 10, 20, 30]  — cycles twice
cl.delete_value(20)
print(cl.to_list(4))    # [10, 30, 10, 30]   — 20 removed, loop continues
```

---

## Step-by-Step Pointer Trace

**Insert at head:**
```
Before: head -> A -> B -> null
Insert X
After:  head -> X -> A -> B -> null
```

**Delete by value (middle):**
```
Before: A -> B -> C -> D -> null
Delete C
After:  A -> B -> D -> null
```

---

## Common Mistakes

**1. Losing the list**
```python
cur = head
cur = cur.next
# head is still safe, but if you overwrite head, the list is lost
```
Always keep a reference to `head`.

**2. Forgetting the empty list case**
```python
if head is None:
    return
```

**3. Skipping nodes when deleting**
If you move both `prev` and `cur` incorrectly, you can jump over nodes.

---

## When to Use Linked Lists

- Frequent inserts/deletes in the middle or at the front
- You do not need random access
- You want predictable memory usage without resizing

---

## Practice Tasks

Work through these in order. Don't skip ahead.

**Task 1 — Build and print**
Create a linked list with values `10 -> 20 -> 30`. Print it as a Python list.

**Task 2 — Insert at head**
Insert `5` at the head. Confirm the list is now `5 -> 10 -> 20 -> 30`.

**Task 3 — Insert at tail**
Insert `40` at the tail. Confirm the list is now `5 -> 10 -> 20 -> 30 -> 40`.

**Task 4 — Delete a value**
Delete `20`. Confirm the list is now `5 -> 10 -> 30 -> 40`.

**Task 5 — Search**
Write a function `contains(value)` that returns `True` if the value is present.

---

## Assignment

Complete all parts below and submit your Python file.

**Part 1 — Singly Linked List (extend the class above)**

1. Add a `length()` method that returns the number of nodes.
2. Add a `reverse()` method that reverses the list in-place.
3. Add a `find_middle()` method that returns the value of the middle node (use the slow/fast pointer technique).

**Part 2 — Doubly Linked List**

Implement a `DoublyLinkedList` class with a `DoublyNode` that has `value`, `next`, and `prev` pointers. Include:

1. `insert_head(value)`
2. `insert_tail(value)`
3. `delete_value(value)` — use the `prev` pointer to avoid tracking it manually
4. `to_list()` — forward traversal
5. `to_list_reversed()` — backward traversal from the tail

**Part 3 — Circular Linked List**

Implement a `CircularLinkedList` class where the last node's `next` points back to `head`. Include:

1. `insert(value)` — insert at tail
2. `delete_value(value)`
3. `print_list(steps)` — print `steps` number of nodes (to avoid infinite loop)
4. Demonstrate cycling through the list twice starting from the head.

**Part 4 — Short Answer (write as comments in your file)**

1. When would you prefer a doubly linked list over a singly linked list?
2. What is one real-world scenario where a circular linked list is the natural choice?
3. What is the main trade-off between linked lists and arrays?

**Submission checklist:**
- [ ] All three list types implemented
- [ ] Each method tested with printed output
- [ ] Short answer questions answered as comments