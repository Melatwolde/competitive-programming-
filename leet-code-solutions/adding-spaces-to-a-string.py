class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        stack = []
        count = 0
        for i in spaces:
            stack.append(s[count:i])
            count = i
        stack.append(s[count:])
        return " ".join(stack)