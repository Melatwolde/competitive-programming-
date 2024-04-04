class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        arr = dict((i, nums.count(i)) for i in set(nums))
        count = 0
        for n in arr.values():
            count += ((n - 1) * n) // 2
        return count
        

        