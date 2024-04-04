class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        targetToRemove = sum(nums) % p
        if (targetToRemove == 0):
            return 0

        minLength = lengthNums = len(nums)
        currSum, dictLengths = 0, defaultdict(lambda : 0)
        for i in range(lengthNums):
            currSum = (currSum + nums[i]) % p
            if (currSum == targetToRemove):
                minLength = min(minLength, i+1)

            if ((currSum - targetToRemove) % p in dictLengths):
                minLength = min(minLength, i - dictLengths[(currSum - targetToRemove) % p])

            dictLengths[currSum] = i

        return minLength if (minLength < lengthNums) else -1