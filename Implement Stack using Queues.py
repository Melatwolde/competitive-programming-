class MyStack:

    def __init__(self):
        self.data = collections.deque()
        

    def push(self, x: int) -> None:
        self.data.append(x)

        for _ in range(len(self.data)-1):
            self.data.append(self.data.popleft())
        

    def pop(self) -> int:
        return self.data.popleft()
        

    def top(self) -> int:
        return self.data[0]
        

    def empty(self) -> bool:
        return not len(self.data)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
