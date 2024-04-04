class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum,max_sum = nums[0],nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in nums[1:]:

            cur_sum = max(i,cur_sum+i) 
            max_sum = max(cur_sum,max_sum)
        return max_sum
                