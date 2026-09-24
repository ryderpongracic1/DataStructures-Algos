from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.left, self.right = deque(), deque()
        # len(left) <= len(right) <= len(left) + 1

    def rebalance(self):
        if len(self.left) > len(self.right):
            val = self.left.pop()
            self.right.appendleft(val)
            # len(left) = len(right)

        elif len(self.right) > len(self.left) + 1:
            val = self.right.popleft()
            self.left.append(val)
            # len(right) = len(left) + 1

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.right) > len(self.left):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        self.rebalance

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if len(self.left) == 0 and len(self.right) == 0:
            return -1
        if len(self.left) == 0:
            val = self.right.pop()
        else:
            val = self.left.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if len(self.right) == 0:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.right:
            return -1
        # if not self.left:
        #     val = self.right.pop()
        val = self.right.pop()
        self.rebalance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()