# DLL Node
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> node
        self.size = capacity

        # dummy head & tail for MRU & LRU access
        self.head = Node()
        self.tail = Node
        self.head.next = self.tail
        self.tail.prev = self.head

    # HELPER methods
    # insert node into DLL
    def insert(self, node):
        prev_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = prev_head
        prev_head.prev = node
    # remove node from DLL
    def remove(self, node):
        next_ptr = node.next
        prev_ptr = node.prev
        next_ptr.prev = prev_ptr
        prev_ptr.next = next_ptr

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.size:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)