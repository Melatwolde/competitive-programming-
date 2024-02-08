class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        remainder_count = [0] * k
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder < 0:
                remainder += k

            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        count += remainder_count[0]

        return count