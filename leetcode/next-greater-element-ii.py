class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n 

        for i in range(2 * n):
            num = nums[i % n]

            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num

            if i < n:
                stack.append(i)

        return result