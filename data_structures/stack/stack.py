from node import Node

class Stack:
    def __init__(self, iter=()):
        self.top = None
        self._len = 0
        for element in iter:
            self.insert(element)

    def insert(self, value):
        self.top = Node(value, self.top)
