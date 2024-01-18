class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lastpos = {nums[0]: 0}
        maxsum = nums[0]
        left = -1
        
        for i in range(1, len(nums)):
            
			# Find index of item if already met
            if nums[i] in lastpos:
                left = max(left, lastpos[nums[i]])
            
            lastpos[nums[i]] = i
            
            nums[i] += nums[i-1]


			
            sub_arr_sum = nums[i] - nums[left] if left != -1 else nums[i]
            maxsum = max(maxsum,  sub_arr_sum)
                
        return maxsum
        
        