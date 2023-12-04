class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
           return "0"
    
        m,n = len(num1), len(num2)
        result = [0] * (m + n)
    
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
               digit1 = int(num1[i])
               digit2 = int(num2[j])
               product = digit1 * digit2
            
               pos1, pos2 = i + j, i + j + 1
               total = product + result[pos2]
            
               result[pos2] = total % 10
               result[pos1] += total // 10
    
    # Remove leading zeros
        while len(result) > 1 and result[0] == 0:
           result.pop(0)
    
        return ''.join(map(str, result))