class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest_candies = max(candies) 
        result = []
        for i in candies:
            count = i + extraCandies
            result.append(count >= greatest_candies)
        return result


