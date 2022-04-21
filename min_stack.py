#https://leetcode.com/problems/min-stack/submissions/
class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.insert(0, val)
    def pop(self) -> None:
        return self.arr.pop(0)
    def top(self) -> int:
        return self.arr[0]
    def getMin(self) -> int:
        return min(self.arr)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
