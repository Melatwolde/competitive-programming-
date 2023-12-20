class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        l, r = 0, 1
        count = 0

        while l < len(nums) - 1:
            if r == len(nums):
                l += 1
                r = l
            if nums[l] == nums[r] and ((l * r) % k == 0) and (l != r):
                print(nums[l], nums[r], l, r)
                count += 1
            r += 1

        return count
