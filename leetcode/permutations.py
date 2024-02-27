class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]

        # path = []
        def backtrack(n = 0):
            if n == len(nums):
                ans.append(nums[:])
            for i in range(n, len(nums)):
                nums[n], nums[i] = nums[i], nums[n]
                backtrack(n + 1)
                nums[n], nums[i] = nums[i], nums[n]

        backtrack()
        return ans