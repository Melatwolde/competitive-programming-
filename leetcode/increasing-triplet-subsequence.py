class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
        # i, j , k = 0 , 1 , 2
        # for i in range(len(nums)):
        #     if nums[i] < nums[j] and nums[j]<nums[k]:
        #         print(i)
        #         i +=1
        #         j +=1
        #         k +=1
        #         return True
        #     else: 
        #         return False
            
        























def increasingTriplet(nums):
    n = len(nums)
    if n < 3:
        return False

    min_num = float('inf')
    second_min = float('inf')

    for num in nums:
        if num <= min_num:
            min_num = num
        elif num <= second_min:
            second_min = num
        else:
            return True

    return False

# Test case 1
nums1 = [1, 2, 3, 4, 5]
print(increasingTriplet(nums1))  # Output: True

# Test case 2
nums2 = [5, 4, 3, 2, 1]
print(increasingTriplet(nums2))  # Output: False

# Test case 3
nums3 = [2, 1, 5, 0, 4, 6]
print(increasingTriplet(nums3))  # Output: True