class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0:
            if n%3==0:
                n/=3
            elif n%3==1:
                n//=3
            else:
                return False
        return True if n==0 else False
            
