import operator
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
