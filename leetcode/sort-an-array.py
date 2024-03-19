class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            merged = []
            l, r = 0, 0
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    merged.append(left_half[l])
                    l += 1
                else:
                    merged.append(right_half[r])
                    r += 1
            merged.extend(left_half[l:])
            merged.extend(right_half[r:])
            return merged

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        return merge(left_half, right_half)