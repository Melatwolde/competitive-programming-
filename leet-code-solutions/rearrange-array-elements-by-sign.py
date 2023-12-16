class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans =[]
        arr1 = []
        arr2 = []
        l ,r = 0 ,0
        for i in nums:
            if i > 0:
                arr1.append(i)
            if i < 0:
                arr2.append(i)
        for l ,r in zip(arr1 , arr2):
            ans.append(l)
            ans.append(r)
        return ans
            



        