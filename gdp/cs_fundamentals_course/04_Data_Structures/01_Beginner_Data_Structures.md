# Beginner Data Structures: The Complete Guide

#  Data Structures 
A data structure is a way of organizing and storing data so it can be accessed, updated, and processed efficiently. It’s like choosing the right container for your data: a list for ordered items, a stack for “last in, first out,” a queue for “first in, first out,” a tree for hierarchies, or a graph for connections. Picking the right data structure makes your programs faster, cleaner, and easier to scale.

---

## 1. Array

### What it is
A fixed-size, ordered collection stored in contiguous (side-by-side) memory. Think of a row of numbered lockers — locker #0, locker #1, locker #2, etc.

### Why it matters
Arrays are the foundation of almost every other data structure. They're simple and extremely fast at accessing data by position.

### Core Operations

| Operation | How it works | Time |
|-----------|--------------|------|
| Read by index | `arr[i]` — jump directly to position i | O(1) |
| Update by index | `arr[i] = value` — replace value at position i | O(1) |
| Insert at end | Add to the last position | O(1) |
| Insert in middle | Shift elements right to make space | O(n) |
| Delete from end | Remove last element | O(1) |
| Delete from middle | Shift elements left to fill gap | O(n) |

### Tiny Example
```python
arr = [10, 20, 30, 40]
print(arr[2])   # → 30 (zero-based index: 0,1,2,3)
arr[2] = 35     # arr is now [10, 20, 35, 40]
```

### When to use
- You need fast random access by position
- The size doesn't change often
- You're working with a fixed amount of data

---

## 2. String

### What it is
A sequence of characters. In most programming languages, a string is essentially an array of characters under the hood.

### Why it matters
Most programs handle text: names, messages, URLs, file paths, user input, etc. Strings are everywhere.

### Core Operations

| Operation | How it works | Example |
|-----------|--------------|---------|
| Access by index | `s[i]` | `"hello"[1]` → `"e"` |
| Concatenate | `s1 + s2` | `"data" + "base"` → `"database"` |
| Substring/Slice | `s[start:end]` | `"python"[1:4]` → `"yth"` |
| Length | `len(s)` | `len("cat")` → `3` |
| Search | `s.find("sub")` | `"hello".find("ell")` → `1` |

### Tiny Example
```python
s = "data"
print(s[1])       # → "a"
print(s[1:3])     # → "at" (index 1 up to but not including 3)
print(len(s))     # → 4
```

### When to use
- Any time you handle text — which is almost always

---

## 3. Linked List

### What it is
A chain of nodes where each node contains a value and a pointer (reference) to the next node. Unlike arrays, nodes can be scattered anywhere in memory — they don't need to be side-by-side.

### Why it matters
Linked lists teach you about references/pointers. They're excellent when you need to insert or delete items frequently, especially at the beginning or middle.

### How it looks in memory
```
Array:  [10][20][30][40]   ← all in one block, side by side
List:   10 → 20 → 30 → 40 → null  ← nodes can be anywhere
```

### Core Operations

| Operation | How it works | Time |
|-----------|--------------|------|
| Insert at head | Create new node, point it to current head | O(1) |
| Insert at tail | Traverse to end, attach new node | O(n) |
| Delete a node | Find previous node, redirect its pointer | O(n) to find, O(1) to delete |
| Traverse | Walk from head to tail following pointers | O(n) |
| Search | Walk through until value is found | O(n) |

### Tiny Example
```
Singly Linked List:  A → B → C → null
- Head points to A
- A points to B
- B points to C
- C points to null (end)
```

### Common Types

| Type | Description |
|------|-------------|
| Singly linked | Each node points to the next node only |
| Doubly linked | Each node points to next AND previous |
| Circular linked | Last node points back to first node |

### When to use
- You insert/delete often, especially at the beginning or middle
- You don't need random access (can't jump to position 5 directly)
- You don't know how much data you'll have in advance

---

## 4. Stack

### What it is
**LIFO** = Last-In, First-Out. Think of a stack of plates — you always take the top plate off. The last plate you put on is the first one you take off.

### Why it matters
Stacks power many everyday programming features: undo/redo, browser back buttons, function calls, and syntax checking.

### Core Operations

| Operation | What it does | Time |
|-----------|--------------|------|
| Push | Add an item to the top | O(1) |
| Pop | Remove and return the top item | O(1) |
| Peek/Top | Look at the top item without removing it | O(1) |
| IsEmpty | Check if stack has no items | O(1) |

### Tiny Example
```python
stack = []
push(1)    # stack: [1]
push(2)    # stack: [1, 2]
push(3)    # stack: [1, 2, 3]
pop()      # returns 3, stack: [1, 2]
peek()     # returns 2, stack still: [1, 2]
```

### Real-world examples
- **Undo (Ctrl+Z):** Each action gets pushed onto stack; undo pops it off
- **Browser back button:** Each page you visit gets pushed; back button pops
- **Function calls:** When a function calls another function, the first is paused and pushed onto call stack

### When to use
- You need to reverse order
- You need to track the most recent item
- You're implementing undo/redo, backtracking, or parsing

---

## 5. Queue

### What it is
**FIFO** = First-In, First-Out. Think of a line at a coffee shop — the first person in line is the first person served.

### Why it matters
Queues are perfect for anything that processes items in order of arrival: print jobs, task scheduling, customer service systems.

### Core Operations

| Operation | What it does | Time |
|-----------|--------------|------|
| Enqueue | Add an item to the back (end) | O(1) |
| Dequeue | Remove and return the front item | O(1) |
| Peek/Front | Look at the front item without removing | O(1) |
| IsEmpty | Check if queue has no items | O(1) |

### Tiny Example
```python
queue = []
enqueue("A")   # queue: [A]
enqueue("B")   # queue: [A, B]
enqueue("C")   # queue: [A, B, C]
dequeue()      # returns A, queue: [B, C]
peek()         # returns B, queue still: [B, C]
```

### Real-world examples
- **Print queue:** Documents print in the order you sent them
- **Customer service:** First caller gets the next available agent
- **Breadth-First Search (BFS):** Exploring a graph level by level

### When to use
- You need to process items in the exact order they arrive
- You're implementing scheduling or buffering

---

## 6. Hash Table (Dictionary / Map / Object)

### What it is
A structure that maps **keys** to **values** using a hash function. The hash function converts a key (like "name") into an index where the value is stored.

### Why it matters
Hash tables are incredibly fast for lookups. They're one of the most useful data structures in programming — you'll use them constantly.

### Core Operations

| Operation | How it works | Time (average) |
|-----------|--------------|----------------|
| Insert | `set(key, value)` — store value at key | O(1) |
| Lookup | `get(key)` — retrieve value for key | O(1) |
| Delete | `delete(key)` — remove key-value pair | O(1) |
| Update | `set(key, newValue)` — replace existing value | O(1) |

### Tiny Example
```python
# Python dictionary / JavaScript object / Java HashMap
person = {
    "name": "Ada",
    "age": 12,
    "city": "London"
}

print(person["age"])     # → 12
person["age"] = 13       # update
person["job"] = "coder"  # insert
del person["city"]       # delete
```

### Visual representation
```
Keys → Hash Function → Index → Value
"name" →  h("name")=2  → index 2 → "Ada"
"age"  →  h("age")=0   → index 0 → 12
"city" →  h("city")=4  → index 4 → "London"
```

### When to use
- You need fast lookups by a key (not by position)
- You don't need items in sorted order
- You want to count frequencies, group data, or cache results

---

## 7. Tree (Basics)

### What it is
A hierarchical structure with a **root** node and **child** nodes. Unlike real trees, computer trees usually have the root at the top and leaves at the bottom.

### Why it matters
Trees model hierarchies (file systems, organization charts) and enable fast searching (Binary Search Trees).

### Key Terminology

| Term | Meaning |
|------|---------|
| Root | Top node with no parent |
| Parent | Node that has child nodes |
| Child | Node that has a parent |
| Leaf | Node with no children |
| Depth | Distance from root (root depth = 0) |

### Binary Search Tree (BST) — The Most Important Tree

**Rule:** For any node, all smaller values go in the LEFT subtree, all larger values go in the RIGHT subtree.

### Tiny Example
```
        10        ← root
       /  \
      5    15     ← children of 10
     / \     \
    3   7     20  ← leaves (no children)
```

**Search for 7:**
1. Start at root (10) → 7 < 10 → go left to 5
2. At 5 → 7 > 5 → go right to 7
3. Found! Only 2 steps (instead of checking all 6 nodes)

### Core Operations (for BST)

| Operation | How it works | Time (balanced) |
|-----------|--------------|-----------------|
| Insert | Compare, go left/right until empty spot found | O(log n) |
| Search | Compare, go left/right until found or null | O(log n) |
| Delete | Find node, rearrange children | O(log n) |

### Traversal Types

| Type | Order | Use case |
|------|-------|----------|
| Inorder | Left → Root → Right | Gets sorted order in BST |
| Preorder | Root → Left → Right | Copying the tree |
| Postorder | Left → Right → Root | Deleting the tree |

### When to use
- You need ordered data that you search frequently
- You're modeling hierarchies (file system, DOM, org chart)
- You need faster search than an array but simpler than a graph

---

## 8. Graph (Basics)

### What it is
A set of **nodes** (vertices) connected by **edges**. Graphs are more flexible than trees — they can have cycles and any node can connect to any other node.

### Why it matters
Graphs model connections and relationships: social networks, road maps, recommendation systems, dependency graphs.

### Key Concepts

| Term | Meaning |
|------|---------|
| Vertex/Node | A point/entity (person, city, web page) |
| Edge | A connection between two vertices (friendship, road, link) |
| Directed | Edges have a direction (one-way street) |
| Undirected | Edges go both ways (friendship) |
| Weighted | Edges have costs (distance, time, price) |

### Types of Graphs

```
Undirected (friendship):      Directed (followers):
A —— B                         A → B
|    |                         ↑   ↓
C —— D                         C ← D
```

### Common Representations

| Method | How it works | Best for |
|--------|--------------|----------|
| Adjacency List | Each node stores list of neighbors | Sparse graphs (few connections) |
| Adjacency Matrix | 2D grid of 0s and 1s | Dense graphs (many connections) |

**Adjacency List Example:**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

### Core Operations

| Operation | How it works | Time |
|-----------|--------------|------|
| Add vertex | Add to vertex list | O(1) |
| Add edge | Add to adjacency list | O(1) |
| BFS (Breadth-First Search) | Explore level by level | O(V + E) |
| DFS (Depth-First Search) | Explore branch fully before backtracking | O(V + E) |

### When to use
- You're modeling connections between entities
- You need shortest path (maps, networking)
- You're doing social network analysis
- You have dependencies between items

---

## Quick Reference Table

| Structure | Access | Insert | Delete | Search | Best For |
|-----------|--------|--------|--------|--------|----------|
| **Array** | O(1) | O(n) | O(n) | O(n) | Random access by index |
| **String** | O(1) | O(n) | O(n) | O(n) | Text manipulation |
| **Linked List** | O(n) | O(1)* | O(1)* | O(n) | Frequent inserts/deletes |
| **Stack** | O(1) | O(1) | O(1) | O(n) | LIFO (undo, backtrack) |
| **Queue** | O(1) | O(1) | O(1) | O(n) | FIFO (scheduling, BFS) |
| **Hash Table** | N/A | O(1) | O(1) | O(1) | Fast key-value lookup |
| **Tree (BST)** | O(log n) | O(log n) | O(log n) | O(log n) | Ordered data, hierarchy |
| **Graph** | O(1) | O(1) | O(1) | O(V+E) | Networks, connections |

*\* O(1) if you already have a reference to the node*

**Time complexity notes:**
- **O(1)** = constant time (fast, doesn't depend on data size)
- **O(log n)** = logarithmic time (very fast, doubles data → +1 step)
- **O(n)** = linear time (slower, 10x data → 10x time)
- **O(V+E)** = depends on vertices (V) and edges (E) in graph

---

## Learning Path (Do in This Order)

```
Phase 1: Foundations
├── 1. Arrays
├── 2. Strings
└── 3. Linked Lists

Phase 2: Linear Structures
├── 4. Stacks
└── 5. Queues

Phase 3: Lookups
└── 6. Hash Tables

Phase 4: Advanced
├── 7. Trees
└── 8. Graphs
```

---

## Practice Plan (How to Actually Learn)

### For Each Structure:

**Step 1: Implement from scratch** (in your language of choice)
- Create the basic structure
- Write the core operations

**Step 2: Code 3 operations manually**
- Don't copy-paste — type them out
- Understand each line

**Step 3: Solve 2 easy problems**
- LeetCode Easy or HackerRank Easy
- Focus on problems that use that specific structure

### Recommended Resources for Practice

| Platform | Best for |
|----------|----------|
| LeetCode | Interview prep (filter by "Easy" and data structure tag) |
| HackerRank | Structured learning paths |
| GeeksforGeeks | Explanations + code examples |

### Sample Problems by Structure

| Structure | Easy Problem to Try |
|-----------|---------------------|
| Array | Two Sum, Best Time to Buy/Sell Stock |
| String | Valid Palindrome, Reverse String |
| Stack | Valid Parentheses |
| Queue | Implement Queue using Stacks |
| Hash Table | Contains Duplicate, Two Sum |
| Tree | Maximum Depth of Binary Tree |
| Graph | Find if Path Exists in Graph |

---

## Quick Summary (One Line Each)

| Structure | One-sentence summary |
|-----------|----------------------|
| **Array** | Ordered list with fast position-based access |
| **String** | Array of characters for text handling |
| **Linked List** | Chain of nodes with fast insert/delete |
| **Stack** | LIFO — last in, first out (like a plate stack) |
| **Queue** | FIFO — first in, first out (like a line) |
| **Hash Table** | Key → Value lookups in O(1) time |
| **Tree** | Hierarchy with fast O(log n) search |
| **Graph** | Flexible connections between nodes |

---

**You're ready to start. Pick one structure, implement it, solve two problems, then move to the next. Happy coding! 🚀**