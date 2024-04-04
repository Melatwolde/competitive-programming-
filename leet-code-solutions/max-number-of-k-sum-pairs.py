class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1
        nums.sort()  
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return count