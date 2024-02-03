class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = [0] * (len(nums) + 1)
        prefix_sums[0] = 1
        odd_count = 0

        for num in nums:
            if num % 2 != 0:
                odd_count += 1

            if odd_count >= k:
                count += prefix_sums[odd_count - k]

            prefix_sums[odd_count] += 1

        return count