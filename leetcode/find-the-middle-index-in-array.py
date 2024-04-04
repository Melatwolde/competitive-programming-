class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        middleindex = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            middleindex[i] = middleindex[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            lsum = middleindex[i]
            rsum = middleindex[-1] - middleindex[i + 1]

            if lsum == rsum:
                return i

        return -1