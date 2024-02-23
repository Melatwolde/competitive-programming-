class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        stack = []
        res = self.getRow(rowIndex-1)
        print(res)
        for i in range(1, len(res) ):
            stack.append(res[i-1] + res[i])
        return [1] + stack + [1]

