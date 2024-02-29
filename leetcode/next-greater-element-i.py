class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack , lookup =[],{}
        for num in nums2:
            while stack and num >stack [-1] :
                lookup [stack.pop()]= num
            stack.append(num)
        while stack:
            lookup [stack.pop()]=-1
        return map (lambda x:lookup[x],nums1)