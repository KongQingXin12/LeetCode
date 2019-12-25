class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        if x is None:
            pass
        else:
            self.l.append(x)

    def pop(self) -> None:
        if self.l is None:
            return 'error'
        else:
            self.l.pop(-1)

    def top(self) -> int:
        if self.l is None:
            return 'error'
        else:
            return self.l[-1]

    def getMin(self) -> int:
        if self.l is None:
            return 'error'
        else:
            return min(self.l)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
