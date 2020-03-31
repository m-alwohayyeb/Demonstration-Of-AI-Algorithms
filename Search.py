from abc import ABC, abstractmethod

class search(ABC):

    def __init__(self, depth = 0, processedNodes = 0, maxStoredNodes = 0):
        self.depth = depth
        self.processedNodes = processedNodes
        self.maxStoredNodes = maxStoredNodes
        super().__init__()

    @abstractmethod
    def solve(self):
        pass