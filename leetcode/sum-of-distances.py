class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        cnt = { }
        cnt1 = { }
        for i in range(len(nums)):
            if(nums[i] in cnt):
                res[i] += cnt[nums[i]][0]*i -(cnt[nums[i]][1])
                cnt[nums[i]][0] += 1 
                cnt[nums[i]][1] += i
            else:
                cnt[nums[i]] = [1,i]
        for i in range(len(nums)-1,-1,-1):
            if(nums[i] in cnt1):
                res[i] += ((cnt1[nums[i]][1])-(cnt1[nums[i]][0]*i))
                cnt1[nums[i]][0] += 1 
                cnt1[nums[i]][1] += i
            else:
                cnt1[nums[i]] = [1,i]
        return res
        
        
                
                
                