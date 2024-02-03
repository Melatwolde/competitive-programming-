class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # n = len(arr)
        # low = 0
        # high = n - 1
        # i = 0

        # while i <= high:
            
        #     if arr[i] == 0:
        #         arr[i], arr[low] = arr[low], arr[i]
        #         low += 1
            
        #     elif arr[i] == 2:
        #         arr[i], arr[high] = arr[high], arr[i]
        #         high -= 1
        #         i -= 1
        #     i += 1

        n = len(nums)
        for i in range(n):
            for j in range (n -i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1] , nums[j]


        

                


