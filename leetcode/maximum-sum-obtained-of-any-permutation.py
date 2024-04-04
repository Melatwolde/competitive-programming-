class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 +7
        pfx = [0] *(len(nums)+1)
        requestsum = []
        for i in requests:
            pfx[i[0]] += 1
            pfx[i[1]+1] -=1
        print(pfx)
        
        pfx_new = []
        cum = 0
        for i in pfx:
            cum += i
            pfx_new.append(cum)
        print(pfx_new)
        
        pfx_ = []
        
        pfx_new.sort(reverse = True)
        nums.sort(reverse = True)
        tot = 0
        for i in range(len(pfx_new) -1):
            tot += pfx_new[i] * nums[i]
        
        return tot % MOD
            