class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num %3 !=0:
            return []
        s = num//3
        return [s-1 , s , s+1]

        