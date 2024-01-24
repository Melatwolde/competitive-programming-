class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # ans = []
        # for i in nums1:
        #     if i in nums2:
        
        #         ans.append(i)
        # return min(ans)

        l , r = 0 ,0
        # stac = []
        while l< len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l+=1
                
            elif nums1[l] > nums2[r]:
                r +=1
            else:
                return nums1[l]
        return -1 