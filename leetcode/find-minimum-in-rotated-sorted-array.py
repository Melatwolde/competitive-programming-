class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        l , r = 0 , len(nums)-1
        curr = float('inf')
        while l <= r:

            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                curr = min(curr, nums[mid])
                r = mid - 1
            else:
                curr = min(curr, nums[l])
                l = mid + 1

        return curr
