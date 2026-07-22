'''
- DLL to track LRU key
- hashmap to track key -> node & hashmap to track frequency -> nodes with that frequency
'''
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next, self.prev = None, None
        self.freq = 1
class DLL:
    def __init__(self):
        # dummy pts for O(1) access to LRU
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0 # how many nodes in DLL for this frequency

    def add_front(self, node):
        old_ptr = self.head.next
        self.head.next, node.next = node, old_ptr
        node.prev, old_ptr.prev = self.head, node
        self.size += 1

    def remove(self, node):
        prev_ptr, next_ptr = node.prev, node.next
        prev_ptr.next, next_ptr.prev = next_ptr, prev_ptr
        self.size -= 1

    def pop_tail(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {} # key -> Node
        self.freq_map = collections.defaultdict(DLL) # freq -> nodes at that freq
    
    def _bump(self, node):
        freq = node.freq

        # self.remove(node)
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

            # only check min_freq AFTER removing a node from its DLL
            # & only update min_freq if DLL is empty
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._bump(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self._bump(node)
            return

        if self.capacity <= len(self.cache):
            lru = self.freq_map[self.min_freq].pop_tail()
            del self.cache[lru.key]
        node = Node(key, value)
        self.min_freq = 1
        self.freq_map[1].add_front(node)
        self.cache[key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)