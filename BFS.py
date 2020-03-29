from queue import Queue as Queue
from Node import Node

class BFS(object):

    def __init__(self):
        pass
    
    def BFS(self,initial_state):   
        start_node = Node(initial_state, None, None, 0)

        if start_node.goal_test().all():
            return start_node.find_solution()

        frontier = Queue() ## List Stack
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
                return node.find_solution()
            print("Depth = {0} \n".format(node.depth))
            print("{0}".format(node.display()))
            print(star)
            explored.append(node.state)
            children = node.generate_child()
            for child in children:
                if child.state not in explored:
                        frontier.put(child)

        return
