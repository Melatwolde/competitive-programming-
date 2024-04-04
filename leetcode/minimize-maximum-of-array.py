class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum = 0
        stack = []
        for i in range(len(nums)):
            cum += nums[i]
            avg = cum / (i+1)
            stack.append(ceil(avg))

        return max(stack)