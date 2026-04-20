# Lesson 3: Stack

A **stack** is a linear data structure that follows **LIFO**: **Last-In, First-Out**. The last item you add is the first item you remove. Think of a stack of plates: you add plates to the top, and you also remove plates from the top.

---

## Learning Goals

By the end of this lesson you should be able to:

- Explain what LIFO means and why stacks are useful.
- Describe the four core stack operations.
- Build a stack in Python using both a list and a linked list.
- Trace stack operations step by step.
- Recognize common stack-based problems in real programs.
- Complete the practice tasks and assignment without looking anything up.

---

## Visual Model

Stacks only allow access at **one end**: the **top**.

```text
Top
 |
 v
+----+
| 30 |
+----+
| 20 |
+----+
| 10 |
+----+
```

If we `push(40)`, it goes on top:

```text
Top
 |
 v
+----+
| 40 |
+----+
| 30 |
+----+
| 20 |
+----+
| 10 |
+----+
```

If we `pop()`, `40` is removed first.

---

## Why Stacks Matter

Stacks appear everywhere in programming:

- **Undo/redo systems** store recent actions.
- **Browser back buttons** remember page history.
- **Function calls** use the call stack.
- **Syntax checking** uses stacks to match brackets like `()`, `[]`, and `{}`.
- **Backtracking algorithms** often push states and pop them when needed.

---

## Key Properties

| Property | What it means |
|---|---|
| **LIFO order** | The last item added is removed first. |
| **Single access point** | You only add/remove from the top. |
| **Fast top operations** | Push, pop, and peek are all O(1). |
| **Restricted access** | You cannot directly access the middle like an array index. |

---

## Core Operations

| Operation | What it does | Time |
|---|---|---|
| `push(x)` | Add `x` to the top | O(1) |
| `pop()` | Remove and return the top item | O(1) |
| `peek()` / `top()` | Return the top item without removing it | O(1) |
| `is_empty()` | Check whether the stack has no items | O(1) |

---

## Stack vs Queue

These are often confused, so keep the rule clear:

| Structure | Rule | Example |
|---|---|---|
| **Stack** | LIFO | Undo history |
| **Queue** | FIFO | People waiting in line |

```text
Stack:  push A, push B, push C -> pop gives C first
Queue:  enqueue A, enqueue B, enqueue C -> dequeue gives A first
```

---

## Python Implementation 1: Stack Using a List

In Python, the easiest stack is a `list`:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# --- Usage ---
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)       # [10, 20, 30]
print(s.peek())      # 30
print(s.pop())       # 30
print(s.items)       # [10, 20]
print(s.is_empty())  # False
```

> In Python, `append()` and `pop()` at the end of a list are O(1) amortized, which makes `list` a good stack implementation.

---

## Python Implementation 2: Stack Using a Linked List

This version helps you understand the structure more deeply. The **head** of the linked list acts as the **top** of the stack.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def to_list(self):
        out = []
        cur = self.top
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out


# --- Usage ---
ls = LinkedStack()
ls.push(10)
ls.push(20)
ls.push(30)
print(ls.to_list())   # [30, 20, 10]  (top to bottom)
print(ls.peek())      # 30
print(ls.pop())       # 30
print(ls.to_list())   # [20, 10]
```

---

## Step-by-Step Trace

Start with an empty stack:

```text
[]
```

Push `1`:

```text
[1]
```

Push `2`:

```text
[1, 2]
```

Push `3`:

```text
[1, 2, 3]
```

Pop:

```text
returns 3
stack becomes [1, 2]
```

Peek:

```text
returns 2
stack stays [1, 2]
```

The key idea is that only the **rightmost/top** element is touched.

---

## Real-World Examples

### 1. Undo Feature

Every new action is pushed onto the stack.

```text
Type A
Type B
Delete B
```

Undo pops the most recent action first.

### 2. Browser Back Button

Each visited page is pushed:

```text
Home -> Products -> Checkout
```

Pressing back pops `Checkout`, then `Products`.

### 3. Function Call Stack

If `main()` calls `login()`, and `login()` calls `validate()`, the stack looks like:

```text
Top -> validate()
       login()
       main()
```

When `validate()` finishes, it is popped off first.

### 4. Bracket Matching

For `"([{}])"`, each opening bracket is pushed. Each closing bracket must match the most recent opening bracket on top of the stack.

---

## Common Mistakes

**1. Popping from an empty stack**
```python
stack = []
stack.pop()   # IndexError in plain Python list
```

Always check first:

```python
if stack:
    stack.pop()
```

**2. Using the wrong end of a list**
```python
stack.append(10)
stack.append(20)
stack.pop(0)   # Wrong for stack behavior
```

`pop(0)` removes from the front, which is slow and breaks the top-of-stack idea.

**3. Confusing stack with queue**

If the first item added is the first item removed, that is a **queue**, not a stack.

**4. Forgetting that peek does not remove**
```python
top = stack[-1]   # looks at top only
```

If you need to remove the item too, use `pop()`.

---

## When to Use a Stack

- You need to reverse order naturally.
- You only care about the most recent item.
- You are solving undo/redo problems.
- You are checking balanced symbols like parentheses.
- You are doing backtracking or depth-first search.

---

## Practice Tasks

Work through these in order. Don't skip ahead.

**Task 1 — Basic push and pop**
Create a stack and push `10`, `20`, and `30`. Pop once and print the result.

**Task 2 — Peek**
After Task 1, print the top item without removing it.

**Task 3 — Is empty**
Keep popping until the stack is empty. Print `True` or `False` after each pop using `is_empty()`.

**Task 4 — Reverse a word**
Use a stack to reverse the word `"STACK"` so the result becomes `"KCATS"`.

**Task 5 — Balanced parentheses**
Write a function that returns `True` if a string has balanced parentheses:

```python
"(())"      -> True
"(()"       -> False
")("        -> False
```

**Task 6 — Explain the use case**
Why is a stack a better choice than a queue for an undo feature?

---

## Assignment

Complete all parts below and submit your Python file.

**Part 1 — Build a stack class**

Create a `Stack` class with these methods:

1. `push(value)`
2. `pop()`
3. `peek()`
4. `is_empty()`
5. `size()`

**Part 2 — Use the stack to solve problems**

Write functions for:

1. Reversing a string using a stack
2. Checking if parentheses are balanced
3. Simulating an undo system for a short list of actions

**Part 3 — Linked-list version**

Implement the stack again using a linked list with a `Node` class.

**Part 4 — Short Answer (write as comments in your file)**

1. Why are push and pop O(1) in a stack?
2. What makes a stack different from a queue?
3. Name two real-world systems that use stack behavior.

**Submission checklist:**
- [ ] Stack class implemented
- [ ] Linked-list stack implemented
- [ ] All methods tested with printed output
- [ ] Practice problems solved
- [ ] Short answer questions answered as comments

---

## Quick Summary

- A stack follows **Last-In, First-Out (LIFO)**.
- You only interact with the **top** of the stack.
- `push`, `pop`, `peek`, and `is_empty` are the essential operations.
- Stacks are ideal for **undo**, **backtracking**, **function calls**, and **syntax matching**.
