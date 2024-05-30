# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        n = len(nums)
        nonnegative= (1 << maximumBit) - 1 
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        answer = []
        
        
        for i in range(n-1, -1, -1):
            k = xor_sum ^ nonnegative
            answer.append(k)
            xor_sum ^= nums[i]  
        return answer
