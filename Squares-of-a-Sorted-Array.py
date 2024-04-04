class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack=[]
        for i in nums:
            stack.append(i**2)

        return sorted(stack)
