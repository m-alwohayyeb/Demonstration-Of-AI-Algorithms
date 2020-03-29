from queue import LifoQueue as Stack
from Node import Node

class IDFS(object):

    def __init__(self):
        pass
    
    def IDFS (self,initial_state):
        d=2
        sol=None
        while sol == None:
            sol = self.DLFS(initial_state,d)
            d= d + 1
        return sol.find_solution
        


    def DLFS(self,initial_state , Depth ):   
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
            if ( node.depth <= Depth and node.state not in explored):
                explored.append(node.state)
                children = node.generate_child()
                for child in children:
                    if child.state not in explored:
                            frontier.put(child)

        return
