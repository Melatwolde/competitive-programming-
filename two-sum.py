class solution:
    def twosum(self,nums,target):
        lookup={}
        for i in enumerate(nums):
            iftarget-num in lookup:
                return[lookup[target-num],i]
            lookup[num]=i
        
