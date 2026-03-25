""""
from collections import deque 

def bd(graph, start, goal):
    #check if values 
    if start == goal :
        return 0
    
    front = {start}
    back = {goal}
    visited_front = {start}
    visited_back = {goal}
    dist = 0 

    while front and back:
        dist +=1

        #expansion 
        if len(front) > len(back):
            back , front = front, back
            visited_front, visited_back = visited_back, visited_front

"""




