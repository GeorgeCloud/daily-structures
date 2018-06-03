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

    def remove(self, value):
        """Removes first occurrence of node by specified value."""
        # Check if empty, add feature to handle if user indexes null.get_value()
        if value == self.head.get_value:
            self.head = self.head._next
            return True

        runner = self.head
        while runner._next._next is not None:
            if value == runner._next.get_value():
                runner._next = runner._next._next
                return True
            else:
                runner = runner._next
        return False
