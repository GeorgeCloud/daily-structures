class HashTable:
    """Hash Table generated from arrays rather than linkedlists. Overwrites
        existing element with same hash value."""
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.buckets = [[] for _ in range(self.max_size)]
    
    def hash(self, key):
        """Creates basic hash for elements to be inserted."""
        return sum([ord(i) for i in key]) % self.max_size
    
    def insert(self, key, value):
        """Inserts key and value pairs into hash table. Overwrites existing
            element with same hash value."""
        self.buckets[self.hash(key)] = {key: value}
    
    def find(self, key):
        """Returns value associated with key if found else False."""
        if self.buckets[self.hash(key)]:
            return self.buckets[self.hash(key)].get(key)
        return None
    
    def remove(self, key):
        """Removes key and sets it to empty placeholder."""
        self.buckets[self.hash(key)] = []
