class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []

        for num1 in nums1:
            found = False
            for num2 in nums2:
                if num2 == num1:
                    found = True
                if found and num2 > num1:
                    result.append(num2)
                    break
            else:
                result.append(-1)

        return result
