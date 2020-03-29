import numpy as np
import math

class PriorityQueue(object):

    # contructor.
    def __init__(self):
        self.queue = []

    # Calculates the heuristic cost from the current state to the goal state.
    def h(self, start, goal):

        size  = int(math.sqrt(len(start)))
        start = np.reshape(np.array(start), (size, size))
        goal  = np.reshape(np.array(goal),  (size, size))
        temp  = 0

        for i in range(0, size):
            for j in range(0, size):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp += 1
        return temp

    # Calculates the actual accumulative cost from the start to the current state.
    def g(self, state):
        return state.depth

    # Calculates the actual accumulative cost from the start to the current state
    # Plus the heuristic cost from the current state to the goal state.
    def f(self, node):
        return self.h(node.state, node.goal_state()) + self.g(node)

    # Returns the default print fromat for the PriorityQueue calss.
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # Checks if the PriorityQueue is empty or not.
    def is_empty(self):
        return len(self.queue) == []

    # Adds new nodes to the PriorityQueue with a custom priority.
    def push(self, sent_state, priority):
        self.queue.append([priority, sent_state])## [priority,state]
       
    # Retrives and returns the node with the best priority.
    def pop(self):
        minimum = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[minimum][0]: ## [][0] -->  priority
                minimum = i
            
        temp = self.queue[minimum]
        del self.queue[minimum]
        
        return temp
        

