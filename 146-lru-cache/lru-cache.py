class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prev_head = self.head.next
        prev_head.prev = node
        node.next = prev_head
        node.prev = self.head
        self.head.next = node

    def remove(self, node):
        next_ptr, prev_ptr = node.next, node.prev
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
            node.val = value
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.size:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)