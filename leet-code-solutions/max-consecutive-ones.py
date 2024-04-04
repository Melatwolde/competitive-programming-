class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        count=0
        for i in nums:
            if i ==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count =0
        return max_count
