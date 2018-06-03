from node import Node

class SList:
    def __init__(self, data=()):
        self.head = None
        self._len = 0
        for element in data[::-1]:
            self.insert(element)

    def insert(self, value):
        self.head = Node(value, self.head)
        self._len += 1
