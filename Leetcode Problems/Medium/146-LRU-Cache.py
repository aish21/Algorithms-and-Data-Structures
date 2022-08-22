'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.cache = deque()

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            self.put(key, self.dict[key])
            return self.dict[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            self.dict[key] = value
            self.cache.remove(key)
            self.cache.append(key)
        else:
            if len(self.dict) == self.capacity:
                keytoremove = self.cache[0]
                self.cache.remove(keytoremove)
                del(self.dict[keytoremove])

            self.cache.append(key)
            self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)