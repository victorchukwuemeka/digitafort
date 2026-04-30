# Graphs — Basics Course

---

## Lesson 1 — What Is a Graph?

A graph is a set of **nodes** (also called vertices) connected by **edges**. It's the most flexible data structure for modeling relationships — unlike trees, graphs can have cycles, and any node can connect to any other node.

```
A —— B
|    |
C —— D
```

Here, `A`, `B`, `C`, `D` are nodes. The lines between them are edges. This could represent cities connected by roads, people connected by friendships, or pages connected by links.

> Graphs power some of the most important technology in the world: Google Maps finds your route using graph algorithms, Facebook models friendships as a graph, and package managers resolve dependencies using graphs.

---

## Lesson 2 — Key Terminology

| Term          | Meaning                                                        |
|---------------|----------------------------------------------------------------|
| Vertex / Node | A point or entity — a person, city, web page, etc.            |
| Edge          | A connection between two vertices                              |
| Directed      | Edges have a direction (A → B, but not B → A)                 |
| Undirected    | Edges go both ways (A — B means A ↔ B)                        |
| Weighted      | Edges carry a cost — distance, time, price, etc.               |
| Cycle         | A path that starts and ends at the same node                   |
| Degree        | How many edges connect to a node                               |
| Path          | A sequence of nodes connected by edges                         |

### Directed vs undirected

```
Undirected (friendship):      Directed (Twitter follows):
A —— B                         A → B
|    |                         ↑   ↓
C —— D                         C ← D
```

In the undirected graph, if A knows B, then B knows A. In the directed graph, A follows B doesn't mean B follows A.

### Weighted graph example

```
   A ——4—— B
   |       |
   2       1
   |       |
   C ——3—— D
```

Each edge now has a cost. The shortest path from A to D isn't necessarily the one with the fewest edges — it's the one with the lowest total weight.

---

## Lesson 3 — Representing a Graph in Code

You can't store a graph the way you'd store a list. You need a way to record which nodes exist and which are connected. Two main approaches:

### Adjacency List — store each node's neighbors

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

Each key is a node. Its value is the list of nodes it connects to. This is the most common representation and works well when most nodes aren't connected to each other (sparse graphs).

### Adjacency Matrix — a 2D grid of connections

```
    A  B  C  D
A [ 0  1  1  0 ]
B [ 1  0  0  1 ]
C [ 1  0  0  1 ]
D [ 0  1  1  0 ]
```

`1` means an edge exists, `0` means it doesn't. Easy to check if two specific nodes are connected, but wastes space when connections are sparse.

### Which to use?

| Representation   | Space    | Check edge  | List neighbors | Best for              |
|------------------|----------|-------------|----------------|-----------------------|
| Adjacency List   | O(V + E) | O(degree)   | O(degree)      | Sparse graphs         |
| Adjacency Matrix | O(V²)    | O(1)        | O(V)           | Dense graphs          |

> In most real-world graphs (social networks, maps), nodes connect to only a small fraction of all other nodes. Adjacency lists are almost always the right default.

---

## Lesson 4 — Traversal: BFS and DFS

Traversal means visiting every node in the graph. There are two fundamental strategies.

### BFS — Breadth-First Search

Explore level by level. Visit all neighbors before going deeper.

```
Graph:          BFS from A:
A — B           Visit A
|   |           Visit B, C  (neighbors of A)
C — D           Visit D      (neighbor of B and C)
```

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')  # → A B C D
```

**Use BFS when:** you want the shortest path (fewest edges) between two nodes.

---

### DFS — Depth-First Search

Follow one branch all the way to the end before backtracking.

```
Graph:          DFS from A:
A — B           Visit A
|   |           Go deep: A → B → D → C
C — D           Backtrack as needed
```

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, 'A')  # → A B D C
```

**Use DFS when:** you want to explore all possible paths, detect cycles, or solve puzzles (mazes, sudoku).

### BFS vs DFS at a glance

| Feature            | BFS                        | DFS                         |
|--------------------|----------------------------|-----------------------------|
| Strategy           | Level by level             | One branch at a time        |
| Data structure     | Queue                      | Stack (or recursion)        |
| Finds shortest path| ✅ Yes (unweighted graphs) | ❌ Not guaranteed           |
| Memory usage       | More (stores all neighbors)| Less (stores one path)      |
| Time complexity    | O(V + E)                   | O(V + E)                    |

---

## Lesson 5 — When to Use a Graph

Use a graph when:

- You're modeling **connections or relationships** between entities — friends, links, dependencies
- You need to find the **shortest path** — GPS navigation, network routing
- You need to detect **cycles** — e.g. circular dependencies in build systems
- You're ranking pages or nodes by **influence** — PageRank, recommendation engines
- You want to find **connected components** — which nodes can reach each other

Don't reach for a graph when:

- Your data is inherently **hierarchical with one root** — a tree is simpler and more structured
- You only need **key-value lookups** — a hash table is much faster and simpler
- Relationships are strictly **sequential** — use a list or queue

---

## Quick Reference

```
Graph Cheat Sheet
─────────────────────────────────────────────────
Types
  Undirected  → edges go both ways (A — B)
  Directed    → edges have direction (A → B)
  Weighted    → edges have costs

Representations
  Adjacency list    → dict of neighbor lists   (default)
  Adjacency matrix  → 2D grid of 0s and 1s     (dense graphs)

Traversal
  BFS  → queue, level by level, finds shortest path
  DFS  → stack/recursion, explores fully before backtracking

Complexity (V = vertices, E = edges)
  BFS / DFS    → O(V + E)
  Add vertex   → O(1)
  Add edge     → O(1)
─────────────────────────────────────────────────
```

---

## Quiz — Test Yourself

**Q1.** What is the difference between a directed and an undirected graph?

- A) Directed graphs can have cycles; undirected graphs cannot
- B) In a directed graph, edges have a specific direction; in undirected, they go both ways
- C) Directed graphs are faster to traverse

> **B** — Direction is the key difference. A directed edge A → B means you can go from A to B, but not necessarily back. An undirected edge A — B means both directions are open.

---

**Q2.** You want to find the shortest path (by number of edges) between two nodes. Which algorithm do you use?

- A) DFS
- B) BFS
- C) Either — they produce the same result

>**B** — BFS explores level by level, so the first time it reaches the destination it has found the shortest path. DFS may find a path but not necessarily the shortest one.

---

**Q3.** You have a graph with 1,000 nodes but each node connects to only 2 or 3 others on average. Which representation is more appropriate?

- A) Adjacency matrix
- B) Adjacency list

> **B** — An adjacency matrix would allocate a 1,000 × 1,000 grid (1 million entries) mostly filled with zeros. An adjacency list only stores the actual connections, which is far more efficient for sparse graphs.

---

**Q4.** Which of the following is NOT a real-world use case for graphs?

- A) Finding the fastest route between two cities
- B) Storing a sorted list of numbers for binary search
- C) Modeling who follows whom on a social network

>  **B** — Sorted lists for binary search are best handled by arrays or binary search trees. The other two are classic graph problems.

---

**Q5.** In DFS, what happens when you reach a node with no unvisited neighbors?

- A) The algorithm stops entirely
- B) You backtrack to the previous node and continue from there
- C) You restart from the root

>  **B** — DFS backtracks. It goes back to the most recent node that still has unvisited neighbors and continues exploring from there.

---

*End of course. You now understand what graphs are, how to represent them, how BFS and DFS traversal works, and when graphs are the right tool.*