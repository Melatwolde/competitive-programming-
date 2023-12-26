class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int(''.join(map(str, digits)))
        return [int(digit) for digit in str(result + 1)]
