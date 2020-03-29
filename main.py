from AStarAlgo import *
from DFS import *
from BFS import *
from IDFS import *
from GreadySearch import *
import time
from GenerateState import GenerateState

state =GenerateState()

a = AStarAlgo()
d = DFS()
b = BFS()
i = IDFS()
g = GreadySearch()

# tmp = state.generate(3)
# print(tmp)
state=[
    4,7,2,
    5,0,3,
    6,8,1
]

start = time.time()
sol = a.a_star_algorithm(state)
print(f'Time: {time.time() - start}')
print(sol)
time.sleep(10.0)

# start = time.time()
# sol = d.DFS(state)
# print(f'Time: {time.time() - start}')
# print(sol)
# time.sleep(10.0)

start = time.time()
sol = b.BFS(state)
print(f'Time: {time.time() - start}')
print(sol)
time.sleep(10.0)

start = time.time()
sol = i.IDFS(state)
print(f'Time: {time.time() - start}')
print(sol)
time.sleep(10.0)

start = time.time()
sol = i.DLFS(state, 10)
print(f'Time: {time.time() - start}')
print(sol)
time.sleep(10.0)

start = time.time()
sol = g.gready_search_algorithm(state)
print(f'Time: {time.time() - start}')
print(sol)
time.sleep(10.0)