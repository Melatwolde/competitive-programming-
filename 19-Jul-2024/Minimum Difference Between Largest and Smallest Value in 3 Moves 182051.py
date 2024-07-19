# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        s1 = nums[-1] - nums[3]     
        s2 = nums[-2] - nums[2]       
        s3 = nums[-3] - nums[1]       
        s4 = nums[-4] - nums[0]      
        return min(s1, s2, s3, s4)