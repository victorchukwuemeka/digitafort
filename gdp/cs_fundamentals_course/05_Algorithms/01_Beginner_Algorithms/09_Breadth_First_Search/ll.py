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








from collections import deque 


def ladder_len(begin_w, end_w, word_l)->str :
    #checking the data in the list 
    if end_w not in word_l:
        return 0 
    
    #flag s needed 
    queue = deque([(begin_w, 1)])
    visited = {begin_w}

    #check the queue before popping
    while queue:
        word, step = queue.popleft()

        #checking the ch in the word list 
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz" :
                #generate new word
                new_w = word[:i] + ch + word[i+1:]
                #compare the new with the  end
                if new_w == end_w:
                    return step +1 
                #adding visited and the queue
                if new_w in word_l and new_w not in visited :
                    visited.add(new_w)
                    queue.append(new_w, step +1)
    return 0


