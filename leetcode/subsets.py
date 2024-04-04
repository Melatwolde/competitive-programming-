class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        res = []

        def back(i):
            if i >= len(nums):
                sub.append(res.copy())
                return

            res.append(nums[i])
            back(i + 1)
            res.pop()
            back(i + 1)

            
        back(0)
        return sub