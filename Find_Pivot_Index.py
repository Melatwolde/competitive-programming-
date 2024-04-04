class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pfxsum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pfxsum[i] = pfxsum[i - 1] + nums[i - 1]
        for i in range(len(nums)):
            left = pfxsum[i]
            right = pfxsum[-1] - pfxsum[i + 1]
            if left == right:
                return i
        return -1
