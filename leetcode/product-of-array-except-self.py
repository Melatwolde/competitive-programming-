class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = 1, 1
        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans