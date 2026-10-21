import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.indices = {}

    def insert(self, val):
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        
        idx_to_remove = self.indices[val]
        last_element = self.data[-1]
        
        self.data[idx_to_remove] = last_element
        self.indices[last_element] = idx_to_remove
        
        self.data.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        return random.choice(self.data)
