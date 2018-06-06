class Node:
    def __init__(self, val, next=None):
        self.value = val
        self._next = next

    def get_value(self):
        return self.value
