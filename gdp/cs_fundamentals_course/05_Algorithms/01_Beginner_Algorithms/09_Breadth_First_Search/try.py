
"""
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    result = []

    while queue:
        node = queue.popleft()       
        result.append(node)          

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result








# Usage
print(bfs(graph, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F']

"""




"""
from collections import deque

def bfs(graph, start):
    visited = set()
    qu = deque()

    visited.add(start)
    qu.append(start)

    r = []

    while qu : 
        node = qu.popleft()
        r.append(node)

        for n in graph[node]:
            if n not in visited :
                visited.add(n)
                qu.append(n)
    return r

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
}

print(bfs(graph,"A"))
"""



#from collections import deque

#creating our tree node 
"""
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val 
        self.right = right
        self.left = left 




name = 8989
for i in name :
    print(i)

"""


"""
class Salah():
    def eyes(self):
        print(f"He  can see")


class Serah(Salah):
    def name(self):
        print("okay ")



person = Serah()
ll = person.eyes()
print(ll)
"""

"""
from collections import deque

def num_i(grid):
    #checking the content of the grid 
    if not grid:
        return 0
    #creating a row and cols 
    rows,cols = len(grid), len(grid[0])
    visited = set()
    islands = 0 

    def bfs(r,c):
       q = deque([(r,c)])
       visited.add((r,c))
       while q :
           row, col = q.popleft() 
           for dr, dc  in [(0,1),(0,-1),(0,1),(-1,0)]:
               nr, nc = row + dr , col + dc 
               if( 0 <= nr < rows and 0 <= nc < cols   # make sure we are in our grid 
                   and  grid[nc][nr] = '1'
                   and (nr, nc) not in visited):
                   visited.add(nr,nc)
                   q.append((nr,nc))
               
    

    
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols  
                        and grid[nr][nc] == '1'
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands




from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == '1'
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


# --- Test calls ---

grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(num_islands(grid1))  # Expected: 1

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid2))  # Expected: 3

grid3 = [
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
]
print(num_islands(grid3))  # Expected: 5

"""




"""
from collections import deque

def island(grid):
    #check the grid data
    if not grid:
        return 0
    
    #create rows and cols 
    rows, cols = len(grid), len(grid[0])
    #add the visited node
    visited = set()
    #declare the island 
    islands  = 0 
    
    #our bfs search 
    def bfs(r,c):
        #create structure
        queue  = deque([(r,c)])
        visited.add((r,c))

        while queue:
            row, col = queue.popleft()
            for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                
"""


ll = 2
print(type({ll}))