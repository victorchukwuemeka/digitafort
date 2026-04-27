# Queue — Data Structures & Algorithms in Python

---

## 1. What Is a Queue?

A queue is a linear data structure that follows the **FIFO** principle — **First In, First Out**. This means the first element added to the queue is always the first one to be removed. Think of it like a real-world queue (line) at a bank or ticket counter: the person who arrives first is served first.

**Key terminology:**

- **Front** — the end from which elements are removed (dequeued)
- **Rear** — the end where new elements are added (enqueued)
- **FIFO** — First In, First Out: the defining rule of a queue

> A queue is the opposite of a stack (which is LIFO — Last In, First Out). The data structure you choose directly determines the algorithm's behaviour.

### Queue Structure Diagram

Below is a conceptual diagram of a queue with 4 elements:

```
dequeue ←  [ 10 (front) ] → [ 20 ] → [ 30 ] → [ 40 (rear) ]  ← enqueue
```

---

## 2. Core Operations

Every queue supports five fundamental operations. Understanding each one — including their time complexity — is essential.

| Operation            | Description                                | List (Python) | deque |
| -------------------- | ------------------------------------------ | :-----------: | :---: |
| `enqueue(x)`         | Add element x to the rear of the queue     |     O(1)      | O(1)  |
| `dequeue()`          | Remove and return the front element        |  **O(n) !**   | O(1)  |
| `peek()` / `front()` | View the front element without removing it |     O(1)      | O(1)  |
| `is_empty()`         | Return True if the queue has no elements   |     O(1)      | O(1)  |
| `size()`             | Return the number of elements in the queue |     O(1)      | O(1)  |

> ⚠️ **WARNING:** Using a Python list for `dequeue()` calls `pop(0)` which is O(n) because every remaining element must shift one position to the left. For any real application, use `collections.deque` which gives O(1) for both ends.

---

## 3. Python Implementations

### Method 1 — Using a Python List

This is the simplest implementation and is good for understanding the concept. However, it has a performance problem: `dequeue()` uses `pop(0)` which is O(n) because Python must shift every remaining element one step to the left after removal.

> 💡 Use this method only for learning or very small queues. For anything larger, use `collections.deque` (Method 2).

```python
class Queue:
    def __init__(self):
        # Internal list to hold all queue elements
        # Index 0 = front of queue, last index = rear
        self.queue = []

    def enqueue(self, item):
        # append() adds to the END of the list = rear of queue
        # This is O(1) — no shifting needed
        self.queue.append(item)

    def dequeue(self):
        # Guard clause: always check before removing
        # Avoids IndexError on an empty list
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue')
        # pop(0) removes from the FRONT of the list
        # BUT: Python shifts all remaining elements left — this is O(n)!
        return self.queue.pop(0)

    def peek(self):
        # Read the front element WITHOUT removing it
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue[0]   # index 0 is always the front

    def is_empty(self):
        # Returns True if there are no elements in the queue
        return len(self.queue) == 0

    def size(self):
        # Number of elements currently in the queue
        return len(self.queue)


# ── Usage ──
q = Queue()
q.enqueue(10)    # queue: [10]
q.enqueue(20)    # queue: [10, 20]
q.enqueue(30)    # queue: [10, 20, 30]

print(q.dequeue())  # Output: 10  (first in, first out)
print(q.peek())     # Output: 20  (front element, not removed)
print(q.size())     # Output: 2
print(q.is_empty()) # Output: False
```

---

### Method 2 — Using `collections.deque` (Recommended)

The `deque` (doubly-ended queue) from Python's `collections` module is implemented internally as a doubly linked list. This gives O(1) performance for adding and removing from both ends. This is the standard, recommended approach for queues in Python.

> ✅ `collections.deque` is the go-to choice. It is part of Python's standard library — no installation needed. Use it whenever you implement a queue.

```python
from collections import deque
# deque = doubly-ended queue (pronounced 'deck')
# Built on a doubly-linked list — O(1) at both ends

class Queue:
    def __init__(self):
        # Create an empty deque to use as our queue
        self.queue = deque()

    def enqueue(self, item):
        # append() adds to the RIGHT side = rear of our queue
        # O(1): no shifting, just a pointer update in the linked list
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty queue')
        # popleft() removes from the LEFT side = front of our queue
        # O(1): much better than list's pop(0) which is O(n)
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        # deque supports index access — index 0 is always the front
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __repr__(self):
        # __repr__ is the 'developer-facing' string representation
        # Useful for debugging: print(q) shows the full queue state
        return f'Queue(front -> {list(self.queue)} -> rear)'


# ── Usage ──
q = Queue()
q.enqueue('Alice')   # queue: ['Alice']
q.enqueue('Bob')     # queue: ['Alice', 'Bob']
q.enqueue('Carol')   # queue: ['Alice', 'Bob', 'Carol']

print(q.dequeue())   # Output: 'Alice'  (first in, first out)
print(q.peek())      # Output: 'Bob'    (front, not removed)
print(q)             # Output: Queue(front -> ['Bob', 'Carol'] -> rear)
```

---

### Method 3 — `queue.Queue` (Thread-Safe)

Python's built-in `queue` module provides a thread-safe queue class. It uses internal locks to prevent race conditions when multiple threads access the queue simultaneously. Use this when building multithreaded applications.

```python
import queue   # Python's built-in thread-safe queue module

# queue.Queue() uses internal mutex locks
# Safe when multiple threads share the same queue object
q = queue.Queue()

# put() = enqueue — adds to the rear
# If maxsize is set and queue is full, put() will BLOCK (wait)
q.put(1)   # queue: [1]
q.put(2)   # queue: [1, 2]
q.put(3)   # queue: [1, 2, 3]

# get() = dequeue — removes from the front
# If the queue is empty, get() will BLOCK until an item is available
print(q.get())     # Output: 1
print(q.qsize())   # Output: 2  (remaining elements)
print(q.empty())   # Output: False

# Optional: set a maximum capacity for the queue
# Once full, put() will block until a consumer calls get()
bounded_q = queue.Queue(maxsize=5)

# Non-blocking version: raises queue.Full or queue.Empty instead of blocking
try:
    bounded_q.put_nowait(99)       # raises queue.Full if full
    item = bounded_q.get_nowait()  # raises queue.Empty if empty
except queue.Full:
    print('Queue is full!')
except queue.Empty:
    print('Queue is empty!')
```

---

### Comparison: Which Method to Use?

| Factor           | `list`          | `collections.deque`             | `queue.Queue`          |
| ---------------- | --------------- | ------------------------------- | ---------------------- |
| `dequeue()` time | O(n)            | O(1)                            | O(1)                   |
| Thread-safe      | No              | No                              | Yes                    |
| Ideal for        | Learning only   | General use / algorithms        | Multithreaded programs |
| Import needed    | None (built-in) | `from collections import deque` | `import queue`         |

---

## 4. Types of Queues

Beyond the basic FIFO queue, there are four important variants, each suited to different problem types.

### 4.1 Simple Queue (Standard FIFO)

The standard queue already covered. Elements are always added at the rear and removed from the front. No special behaviour.

---

### 4.2 Circular Queue

A circular queue uses a fixed-size array where the rear pointer wraps around to the beginning of the array when it reaches the end. This reuses the space freed by dequeue operations, making it memory-efficient for fixed-capacity buffers such as OS I/O buffers, audio streaming, and network packet queues.

> 💡 In a regular queue on an array, dequeuing from the front wastes the slots at the beginning. A circular queue solves this by reusing them via modulo arithmetic.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        # Pre-allocate a fixed-size list, all slots initially None
        self.queue = [None] * capacity
        # front and rear both start at -1 to indicate an empty queue
        self.front = self.rear = -1
        self.size = 0          # track current number of elements

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError('Circular queue is full')
        # Modulo wraps rear back to 0 after the last index
        # Example with capacity=5: after index 4, next is (4+1)%5 = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        if self.front == -1:
            self.front = 0    # first insertion: set front to index 0
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Circular queue is empty')
        item = self.queue[self.front]
        self.queue[self.front] = None  # clear the slot for reuse
        # Advance front — modulo wraps it around the circular buffer
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        return self.queue[self.front]

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return f'CircularQueue({self.queue}) front={self.front} rear={self.rear}'


# ── Usage ──
cq = CircularQueue(4)
cq.enqueue(10)   # [10, None, None, None]  front=0, rear=0
cq.enqueue(20)   # [10, 20, None, None]    front=0, rear=1
cq.enqueue(30)   # [10, 20, 30, None]      front=0, rear=2
cq.dequeue()     # returns 10, front moves to 1
cq.enqueue(40)   # [None, 20, 30, 40]      front=1, rear=3
cq.enqueue(50)   # [50, 20, 30, 40]  rear wraps to 0 (circular!)
```

---

### 4.3 Priority Queue

A priority queue dequeues elements by priority rather than by arrival order. The element with the highest priority (lowest priority number in a min-heap) is always removed first, regardless of when it was inserted.

Python implements this using `heapq`, which maintains a **min-heap**: a binary tree where the parent node is always smaller than or equal to its children. The smallest element is always at the root (index 0).

> 💡 `heapq` is a min-heap by default: the smallest number comes out first. To simulate a max-heap (largest first), store values as negative numbers: `heapq.heappush(heap, -value)`.

```python
import heapq   # Python's heap queue module — implements a min-heap

class PriorityQueue:
    def __init__(self):
        # Internal list treated as a binary heap tree
        # heapq maintains the heap property automatically
        self.heap = []

    def enqueue(self, item, priority):
        # Store as a (priority, item) TUPLE
        # heapq sorts by the FIRST element of the tuple (the priority)
        # Lower priority number = higher urgency (min-heap)
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        # heappop() removes and returns the SMALLEST (priority, item) tuple
        # The heap then re-arranges itself to maintain the heap property
        priority, item = heapq.heappop(self.heap)
        return item   # return just the item; priority was internal metadata

    def peek(self):
        # heap[0] is always the minimum element — no removal
        # Index [1] gives the item; index [0] is the priority
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# ── Usage ──
pq = PriorityQueue()
pq.enqueue('low task',    3)  # priority 3 = least urgent
pq.enqueue('urgent task', 1)  # priority 1 = most urgent
pq.enqueue('medium task', 2)  # priority 2 = middle

# Despite insertion order being 3, 1, 2...
# dequeue() always returns the item with the LOWEST priority number first
print(pq.dequeue())  # Output: 'urgent task'  (priority 1)
print(pq.dequeue())  # Output: 'medium task'  (priority 2)
print(pq.dequeue())  # Output: 'low task'     (priority 3)

# ── Max-Heap: highest priority number exits first ──
max_heap = []
heapq.heappush(max_heap, (-3, 'task C'))  # store as NEGATIVE
heapq.heappush(max_heap, (-1, 'task A'))
heapq.heappush(max_heap, (-5, 'task E'))  # -5 is smallest, so exits first
pri, item = heapq.heappop(max_heap)
print(-pri, item)   # Output: 5 task E  (highest priority exits first)
```

---

### 4.4 Deque — Double-Ended Queue

A deque (doubly-ended queue) allows insertion and removal from both the front and the rear in O(1) time. It is more general than a regular queue and is used for sliding window problems, palindrome checking, and undo/redo functionality.

```python
from collections import deque

dq = deque()

# ── Adding elements ──
dq.append(20)       # Add to the RIGHT (rear)  -> deque([20])
dq.appendleft(10)   # Add to the LEFT (front)  -> deque([10, 20])
dq.append(30)       # Add to the RIGHT (rear)  -> deque([10, 20, 30])

# ── Removing elements ──
dq.popleft()   # Remove from LEFT (front) -> returns 10, deque([20, 30])
dq.pop()       # Remove from RIGHT (rear) -> returns 30, deque([20])

# ── Other useful deque operations ──
dq = deque([1, 2, 3, 4, 5])

# rotate(n): shift all elements n positions to the right
# Negative n shifts to the left
dq.rotate(2)    # deque([4, 5, 1, 2, 3])
dq.rotate(-1)   # deque([5, 1, 2, 3, 4])

# maxlen: automatically discards oldest element when capacity is exceeded
# Useful for keeping a rolling window of recent items
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
    print(list(recent))
# Output: [0], [0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5]
# When full, oldest element on the LEFT is automatically removed
```

---

## 5. Real-World Application: Breadth-First Search (BFS)

BFS is the classic algorithm that requires a queue. It explores a graph or tree level by level, visiting all nodes at distance 1 before any nodes at distance 2, and so on. This guarantees the shortest path in an unweighted graph.

> ✅ The data structure you choose determines the traversal algorithm: a **QUEUE** gives BFS (level-by-level), while a **STACK** gives DFS (depth-first). This is a fundamental insight in algorithms.

### Why BFS Needs a Queue

BFS must process nodes in the order they were discovered — first-come, first-served. A queue enforces this FIFO ordering. Nodes discovered first are processed first, which ensures all nodes at the current depth level are fully explored before we move deeper.

**BFS traversal for the graph `A -> B, C | B -> D, E | C -> F`:**

| Step | Current | Queue after step | Action                                |
| :--: | :-----: | ---------------- | ------------------------------------- |
|  1   |    A    | [B, C]           | Dequeue A. Enqueue neighbours B and C |
|  2   |    B    | [C, D, E]        | Dequeue B. Enqueue neighbours D and E |
|  3   |    C    | [D, E, F]        | Dequeue C. Enqueue neighbour F        |
|  4   |    D    | [E, F]           | Dequeue D. No unvisited neighbours    |
|  5   |    E    | [F]              | Dequeue E. No unvisited neighbours    |
|  6   |    F    | [] (empty)       | Dequeue F. Queue empty — BFS complete |

**Final BFS order:** `A -> B -> C -> D -> E -> F` (level 0, then level 1, then level 2)

### BFS Implementation in Python

```python
from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph.

    Args:
        graph: dict mapping each node to a list of its neighbours
        start: the starting node for traversal
    Returns:
        list of nodes in BFS (level-by-level) order
    """
    # visited set prevents revisiting nodes
    # Without this, we'd loop forever on graphs with cycles
    visited = set()

    # Initialise the queue with the starting node
    # deque is used here — O(1) popleft() is critical for BFS efficiency
    queue = deque([start])
    visited.add(start)    # mark start as visited immediately on enqueue

    order = []   # will store nodes in the order they are visited

    while queue:                          # loop until no more nodes to process
        node = queue.popleft()            # DEQUEUE: process the oldest (front) node
        order.append(node)                # record that we've processed this node

        # Explore all direct neighbours of the current node
        for neighbour in graph[node]:
            if neighbour not in visited:  # only process unvisited neighbours
                visited.add(neighbour)    # mark visited on ENQUEUE (not dequeue)
                queue.append(neighbour)   # enqueue for future processing
                # These neighbours will be processed AFTER all nodes
                # already in the queue (FIFO — this is what makes it BFS)

    return order


# ── Example graph represented as an adjacency list ──
# Each key is a node, the value is a list of its connected neighbours
graph = {
    'A': ['B', 'C'],    # A connects to B and C  (Level 0 -> Level 1)
    'B': ['D', 'E'],    # B connects to D and E  (Level 1 -> Level 2)
    'C': ['F'],         # C connects to F         (Level 1 -> Level 2)
    'D': [],            # D is a leaf node (no outgoing edges)
    'E': [],            # E is a leaf node
    'F': []             # F is a leaf node
}

result = bfs(graph, 'A')
print(result)
# Output: ['A', 'B', 'C', 'D', 'E', 'F']
#
# Level 0: A
# Level 1: B, C  (both neighbours of A)
# Level 2: D, E, F  (neighbours of B and C)


# ── BFS for shortest path ──
def bfs_shortest_path(graph, start, goal):
    """Find the shortest path between start and goal using BFS."""
    # Each queue entry is a PATH (list of nodes), not just a node
    # This lets us reconstruct the full path when we reach the goal
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()    # dequeue the oldest path
        node = path[-1]           # the current node is the last in the path

        if node == goal:
            return path           # found the goal — return the complete path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path + [neighbour]   # extend the path
                queue.append(new_path)           # enqueue the extended path

    return None   # no path found (disconnected graph)

# BFS guarantees this is the SHORTEST path (fewest edges)
print(bfs_shortest_path(graph, 'A', 'F'))  # Output: ['A', 'C', 'F']
```

---

## 6. Real-World Applications of Queues

Queues appear throughout computer science and software engineering. Understanding where queues are used helps you recognise when to reach for them in your own solutions.

| Domain            | Use Case                                                                              | Queue Type Used               |
| ----------------- | ------------------------------------------------------------------------------------- | ----------------------------- |
| Graph Algorithms  | BFS traversal, shortest path in unweighted graphs, social network connection distance | Simple Queue (deque)          |
| Operating Systems | CPU process scheduling (FCFS), I/O request buffering, print spooling                  | Simple Queue / Priority Queue |
| Message Brokers   | Kafka, RabbitMQ, Amazon SQS — durable FIFO message passing between services           | Persistent Queue              |
| Sliding Window    | Maximum/minimum of a sliding window (e.g. LeetCode 239), moving averages              | Deque (double-ended)          |
| Cache Management  | LRU cache (Least Recently Used) — evicts the oldest entry when capacity is reached    | Deque + Hash Map              |
| Networking        | Packet buffering in routers, TCP connection request queues, request rate limiting     | Circular Queue                |
| Web Servers       | HTTP request handling, worker thread pools, async task queues (Celery, Bull)          | Thread-safe Queue             |
| Pathfinding       | Dijkstra's algorithm (shortest path with weights), A\* search for game AI             | Priority Queue (heapq)        |

---

## 7. Practice Problems

Work through these problems in order. Each one builds on the previous and reinforces a different aspect of queue usage.

### Beginner

1. Implement a `Queue` class using two stacks. Enqueue should be O(1); dequeue amortised O(1).
2. Write a function that reverses the order of elements in a queue using only a stack as auxiliary storage.
3. Given a queue, write a function to generate the first N binary numbers (1, 10, 11, 100...) using only a queue.

---

## 8. Summary

| Queue Type        | Defining Characteristic                | Best For             | Python Tool         |
| ----------------- | -------------------------------------- | -------------------- | ------------------- |
| Simple Queue      | FIFO: first inserted = first removed   | BFS, task scheduling | `collections.deque` |
| Circular Queue    | Fixed size, rear wraps around to front | Buffers, streaming   | Custom array class  |
| Priority Queue    | Exits by priority, not arrival order   | Dijkstra, scheduling | `heapq` module      |
| Deque             | O(1) insert and remove at both ends    | Sliding window, LRU  | `collections.deque` |
| Thread-safe Queue | Mutex-locked for concurrent access     | Multithreaded apps   | `queue.Queue`       |

> ✅ **Golden rule:** always use `collections.deque` for queue implementations in Python. It gives O(1) on both ends, is part of the standard library, and is significantly faster than using a plain list.

---
