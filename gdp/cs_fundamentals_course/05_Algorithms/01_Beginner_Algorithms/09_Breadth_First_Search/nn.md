Let me break it down visually:

---

**The Problem**
Given a grid like this:
```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
Count the islands — answer is **3**.

---

**The Idea**
- Walk every cell in the grid
- When you find a `1` (land) you haven't visited → that's a new island
- **Flood fill** all connected land cells so you don't count them again
- Move to next unvisited cell

---

**Line by line:**

```python
if not grid:
    return 0
```
Empty grid → 0 islands, done.

---

```python
rows, cols = len(grid), len(grid[0])
visited = set()
islands = 0
```
- `rows, cols` — grid dimensions
- `visited` — tracks cells already explored
- `islands` — counter

---

```python
def bfs(r, c):
    queue = deque([(r, c)])
    visited.add((r, c))
```
BFS starts at cell `(r, c)` — adds it to queue and marks visited immediately.

---

```python
    while queue:
        row, col = queue.popleft()
```
Keep processing cells until queue is empty — `popleft()` makes it a proper queue (FIFO).

---

```python
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = row + dr, col + dc
```
Check all **4 neighbours** — right, left, down, up:
```
        (row-1, col)
             ↑
(row, col-1) ← [cell] → (row, col+1)
             ↓
        (row+1, col)
```

---

```python
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == '1'
                    and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))
```
Only add neighbour to queue if:
- ✅ Inside grid boundaries
- ✅ Is land (`'1'`)
- ✅ Not already visited

---

```python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '1' and (r, c) not in visited:
            bfs(r, c)
            islands += 1
```
Walk every cell — when you find **unvisited land**:
- Run BFS to flood fill the whole island
- Increment counter by 1

---

**Visual walkthrough:**
```
1 1 0        Step 1: hit (0,0) → BFS floods (0,0)(0,1)(1,0)(1,1) → island 1
1 1 0        Step 2: all those cells now visited, skip them
0 0 1        Step 3: hit (2,2) → BFS floods just (2,2) → island 2
```
**Result: 2 islands** ✅

---

**One thing to note** — you're missing the import at the top:
```python
from collections import deque
```
Without that it will crash. 🚀