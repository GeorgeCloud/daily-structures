from .linked_list import SList, Node

def get_queue(self, value):
    self.head = Node(value, self.head)
    self._len += 1
    return self._len


SList.get_queue = get_queue
