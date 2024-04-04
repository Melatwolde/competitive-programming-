class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        perfixsum =[]
        cum = 0
        for i in nums:
            cum += i
            perfixsum.append(cum)
        return perfixsum