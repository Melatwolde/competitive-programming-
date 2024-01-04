class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        windowsum = sum(nums[:k])
        maxsum = windowsum
        for i in range(k, n):
            windowsum += nums[i] 
            windowsum -= nums[i-k]
            maxsum = max(maxsum , windowsum)

            
        return maxsum/ k

        