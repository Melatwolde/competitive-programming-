class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_ = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_ or val <= self.stack_[-1]:
            self.stack_.append(val)
        
    def pop(self) -> None:
        if self.stack.pop() == self.stack_[-1]:
            self.stack_.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack_[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()