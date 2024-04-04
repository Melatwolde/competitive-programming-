class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        reversed_str = x_str[::-1]
        if x_str == reversed_str:
            return True
        else:
            return False