class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        prefix_sum[0] = 1 
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count

        # l ,r = 0 ,1
        # count = 0
        # while l <len(nums):
        #     if nums[l] or nums[r] == k:
        #         count +=1
                
        #     elif nums[l] + nums[r] == k:
        #         count +=1
        #     l +=1
        #     r +=1
        # return count

        
        

