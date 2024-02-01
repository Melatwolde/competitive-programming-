class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        deleted = False
        max_length = 0
        zeros_count = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1
            
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            max_length = max(max_length, right - left)
            right += 1
        
        return max_length