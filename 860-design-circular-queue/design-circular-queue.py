class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.k = k          # size
        self.front = 0      # pointer
        self.rear = 0       # pointer to first free slot
        self.size = 0       # active queue elements

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.rear] = value
        self.size += 1
        self.rear = (self.rear + 1) % self.k

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.front] = 0
        self.size -= 1
        self.front = (self.front + 1) % self.k

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()