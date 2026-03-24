
"""

from collections import deque

#shortest distance 
def s_d(g,start,end):
    #checking empty data
    if start == end:
        return 0
    
    #marking visited nodes
    visited = { start}

    #structure queue
    queue  = deque([(start,0)])

    while queue :
        #getting our node and distance 
        node, dist = queue.popleft()
        # visit the next node 
        for n in g[node]:
            if n == end :
                return dist + 1
            if n not in visited:
                visited.add((n))
                queue.append((n, dist+1))

    return -1 

"""






from collections import deque


# shortest distance to the exist using multiple route
def update_matric(mat):
    # our grid 
    rows, cols = len(mat), len(mat[0])

    # distance 
    dist  = [[float('inf')] * cols for i in range(rows)]
    # structure fifo
    queue = deque()
     
    #
    for r in range(rows):


