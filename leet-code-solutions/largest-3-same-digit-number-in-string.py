class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        largest_good = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i:i+3] > largest_good:
                    largest_good = num[i:i+3]
        
        return largest_good

        