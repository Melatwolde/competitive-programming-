class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack =[]
        if n%2==0:
            return n
        stack.append(2*n)
        return min(stack)
        