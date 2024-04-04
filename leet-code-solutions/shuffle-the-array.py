class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res=[]
        x = nums[:n]  
        y = nums[n:] 
        for i in range (n):
            res.append(x[i])
            res.append(y[i])
        return res

         