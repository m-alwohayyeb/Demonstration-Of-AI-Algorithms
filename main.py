from AStarAlgo import *
from DFS import *
from BFS import *
from IDFS import *
from GreadySearch import *
from GenerateState import GenerateState
from Node import Node
import numpy as np
import time

a = AStarAlgo()
d = DFS()
b = BFS()
i = IDFS()
g = GreadySearch()

def batch(state, depth = 10):
    
    # A* Search.
    start = time.time()
    sol = a.a_star_algorithm(state)
    print(f'Time: {time.time() - start}')
    print(sol)
    
    time.sleep(5)
    # Gready Search.
    start = time.time()
    g.gready_search_algorithm(state)
    print(f'Time: {time.time() - start}')
    print(sol)
    
    time.sleep(5)
    # Breadth First Search.
    start = time.time()
    sol = b.BFS(state)
    print(f'Time: {time.time() - start}')
    print(sol)
    
    time.sleep(5)
    # Iterative Deapening Search.
    start = time.time()
    sol = i.IDFS(state)
    print(f'Time: {time.time() - start}')
    print(sol)
    
    time.sleep(5)
    # Depth Limited First Search.
    start = time.time()
    sol = i.DLFS(state, depth)
    print(f'Time: {time.time() - start}')
    print(sol)
    
    time.sleep(5)
    # Depth First Search.
    start = time.time()
    sol = d.DFS(state)
    print(f'Time: {time.time() - start}')
    print(sol)
    

def randomState():
    return GenerateState()


# state = [
#     1,2,3,
#     4,5,6,
#     0,7,8
# ]

state = [
    4,7,2,
    5,0,3,
    6,8,1
]

batch(state)




























# -------------------------- Tests --------------------------------- #


# state = [1,2,3,
#          4,0,6
#         ,7,5,8]
# start_node = Node(state, None, None, 0,state.index(0))
# ll = start_node.generate_child()

# for i in ll:
#     print(i.state)


# state = GenerateState()

# print(tmp)
# state=[
#     1,2,3,4,5,0,6,7,8
# ]



# start = time.time()
# sol = a.a_star_algorithm(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# print()

# start = time.time()
# sol = d.DFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# 

# start = time.time()
# sol = b.BFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# 

# start = time.time()
# sol = i.IDFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# 

# start = time.time()
# sol = i.DLFS(state, 10)
# print(f'Time: {time.time() - start}')
# print(sol)
# 

# times = []
# s=[
#     4,7,2,
#     5,0,3,
#     6,8,1
# ]

# s = [ 
#       8,6,7,
#       2,5,4,
#       3,0,1
#     ]

# for i in range(3):
#     start = time.time()
#     sol = a.a_star_algorithm(s)
#     times.append(time.time() - start)
#     print(sol)

# avg = np.average(times)
# print(avg)
