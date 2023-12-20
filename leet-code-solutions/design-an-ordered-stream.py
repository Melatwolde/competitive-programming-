class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n 
        self.ptr = 0  

    def insert(self, idKey: int, value: str):
        idKey -= 1  

        self.stream[idKey] = value

        result = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result

# Example usage:
orderedStream = OrderedStream(5)
print(orderedStream.insert(3, "ccccc"))  # Output: []
print(orderedStream.insert(1, "aaaaa"))  # Output: ["aaaaa"]
print(orderedStream.insert(2, "bbbbb"))  # Output: ["bbbbb", "ccccc"]
print(orderedStream.insert(5, "eeeee"))  # Output: []
print(orderedStream.insert(4, "ddddd"))  # Output: ["ddddd", "eeeee"]



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)