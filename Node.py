import math
import numpy as np

class Node:   
     
    num_of_instances = 0

    def __init__(self, state, parent, action, depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
        Node.num_of_instances += 1 #space
        
    def get_size(self):
        return math.sqrt(len(self.state))

    def goal_state(self):
        goal_state = np.array(range(1,len(self.state)))
        goal_state = np.append(goal_state,0)
        return goal_state

    def display(self):
        list_state = self.state
        string = ""
        for i in range(len(self.state)):
            if (i + 1) % self.get_size() != 0:
                if list_state[i] == 0:
                    string += "|   "
                else:
                    string += ("| %d " % list_state[i])
            else:
                if list_state[i] == 0:
                    string += "|   \n"
                else:
                    string += ("| %d |\n" % list_state[i])
        string += "\n"
        return string

    def __str__(self):
        return self.display()

    def goal_test(self):
        return self.state ==self.goal_state()

    
    def find_legal_actions(self,i, j):
        legal_action = ['LEFT', 'RIGHT','UP', 'DOWN',]

        """UP and DOWN Disable Condition"""
        """LEFT and RIGHT Disable Condition"""
        if j == 0:
            legal_action.remove('LEFT')
        elif j == self.get_size()-1:
            legal_action.remove('RIGHT')

        if i == self.get_size()-1:
            legal_action.remove('DOWN')
        elif i == 0:
            legal_action.remove('UP')
        
        return legal_action

    def generate_child(self):
        children = []
        size = int(self.get_size())
        x = self.state.index(0)
        i = int(x / size)
        j = int(x % size)
        legal_actions = self.find_legal_actions(i, j)
        depth = self.depth + 1

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'UP':
                new_state[x], new_state[x - size] = new_state[x - size], new_state[x]
            elif action is 'DOWN':
                new_state[x], new_state[x + size] = new_state[x + size], new_state[x]
            elif action is 'LEFT':
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'RIGHT':
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            children.append(Node(new_state, self, action, depth))
        return children

    def find_solution(self):## helper functoin, may help us in the web side!
        solution = [self.action]
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]## the last one we added in the first line
        solution.reverse()## solution is ordered from the goal action, so we reverse it !
        return solution
