class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        nums.sort(reverse=True)
        
        largest = nums[0]
        operations = 0
        
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                operations += i+1
        return operations