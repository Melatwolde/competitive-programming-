class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return closest_sum