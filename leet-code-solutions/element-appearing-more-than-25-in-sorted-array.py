class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        nums = Counter(arr)
        for key, value in nums.items():
            if value == max(nums.values()):
                return key