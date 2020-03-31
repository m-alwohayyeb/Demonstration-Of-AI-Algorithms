from PriorityQueue import PriorityQueue
from Node import Node

class GreadySearch(object):

    def __init__(self):
        pass
    
    def gready_search_algorithm(self,initial_state):
        start_node = Node(initial_state, None, None, 0,initial_state.index(0))

        if start_node.goal_test().all():
            return start_node.find_solution()

        frontier = PriorityQueue() ## List queue
        frontier.push(start_node, frontier.h(start_node.state, start_node.goal_state()))
        explored = set()    ## Needs changing, change to set().
        star = "**********************************"
        print("\nInitial State ---------- Depth: {0}".format(start_node.depth))
        while not (frontier.is_empty()):
            v = frontier.pop()
            node = v[-1]
            print("--------------------------------------------------")
            if node.goal_test().all():
                print("***************GOAL STATE FOUND*******************")
                print("\n")
                print(node.display())
                return node.find_solution()
            
            print("Depth = {0} \n".format(node.depth))
            print("{0}".format(node.display()))
            print(star)
            explored.add(tuple(node.state))
            children = node.generate_child()
            for child in children:
                if tuple(child.state) not in explored:
                    frontier.push(child, frontier.h(child.state, child.goal_state()))
        return
