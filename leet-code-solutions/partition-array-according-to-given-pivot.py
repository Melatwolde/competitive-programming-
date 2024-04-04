class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1=[]
        nums2=[]
        nums3 =[]
        for i in nums:
            if  i == pivot:
                nums3.append(i)
            if i < pivot:
                nums1.append(i)
            if i > pivot: 
                nums2.append(i)
        nums1.extend(nums3)
        nums1.extend(nums2)
        return nums1

        