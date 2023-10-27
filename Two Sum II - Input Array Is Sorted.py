class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers) - 1
        while r < l:
            if numbers[r] + numbers[l] == target:
                return [r + 1, l + 1]
            if numbers[r] + numbers[l] < target:
                r += 1
            else:
                l -= 1
            
