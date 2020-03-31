from AStarAlgo import *
from DFS import *
from BFS import *
from IDFS import *
from GreadySearch import *
import time
from GenerateState import GenerateState
from Node import Node
import numpy as np





# state = [1,2,3,
#          4,0,6
#         ,7,5,8]
# start_node = Node(state, None, None, 0,state.index(0))
# ll = start_node.generate_child()

# for i in ll:
#     print(i.state)


state = GenerateState()

a = AStarAlgo()
# d = DFS()
# b = BFS()
# i = IDFS()
# g = GreadySearch()

# print(tmp)
# state=[
#     1,2,3,4,5,0,6,7,8
# ]

# state=[
#     4,7,2,
#     5,0,3,
#     6,8,1
# ]

# # state=[
# #     1,2,3,
# #     4,5,6,
# #     0,7,8
# # ]


# start = time.time()
# sol = a.a_star_algorithm(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# print()

# start = time.time()
# sol = d.DFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# time.sleep(10.0)

# start = time.time()
# sol = b.BFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# time.sleep(10.0)

# start = time.time()
# sol = i.IDFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# time.sleep(10.0)

# start = time.time()
# sol = i.DLFS(state, 10)
# print(f'Time: {time.time() - start}')
# print(sol)
# time.sleep(10.0)

times = []
# s=[
#     4,7,2,
#     5,0,3,
#     6,8,1
# ]

s = [ 
      8,6,7,
      2,5,4,
      3,0,1
    ]

for i in range(3):
    start = time.time()
    sol = a.a_star_algorithm(s)
    times.append(time.time() - start)
    print(sol)

avg = np.average(times)
print(avg)
