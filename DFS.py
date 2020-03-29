from queue import LifoQueue as Stack
from Node import Node

class DFS(object):

    def __init__(self):
        pass
    
    def DFS(self,initial_state):   
        start_node = Node(initial_state, None, None, 0)

        if start_node.goal_test().all():
            return start_node.find_solution()

        frontier = Stack() ## List Stack
        frontier.put(start_node)
        explored = [] ## Needs changing, change to set(). 
        star = "**********************************"
        print("\nInitial State ---------- Depth: {0}".format(start_node.depth))
        while not (frontier.empty()):
            node = frontier.get()
            print("--------------------------------------------------")
            if node.goal_test().all():
                print("***************GOAL STATE FOUND*******************")
                print("\n")
                print(node.display())
                return node
            print("Depth = {0} \n".format(node.depth))
            print("{0}".format(node.display()))
            print(star)
            explored.append(node.state)
            children = node.generate_child()
            for child in children:
                if child.state not in explored:
                        frontier.put(child)

        return
