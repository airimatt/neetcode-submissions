class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left
    
    def remove(self, node):
        p, n = node.prev, node.nxt
        p.nxt = n
        n.prev = p
    
    def insert(self, node):
        p, n = self.right.prev, self.right
        p.nxt = node
        node.prev = p
        n.prev = node
        node.nxt = n


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

        




# notes
# cache: { key : node (node has key, value, prev, and next)}
# have leastRecent and mostRecent pointer pointing to least and most recently used
# get will make key most recently used so delete that one and insert it at the end of the LL
# - have mostRecent point to it
# put will also make key most recently used so insert it at the end of the LL
# - have mostRecent point to it
# if put makes len(cache) > cap then we have to remove the node at the front of the LL where leastRecent is pointing