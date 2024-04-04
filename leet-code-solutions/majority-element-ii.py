class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        for i in set(nums):
            if nums.count(i) > len(nums) // 3:
                res.append(i)
        return res