class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
      leftsum, rightsum = 0, nums.count(1)

      d = {}

      i = 0
      while i <= len(nums):
        score = leftsum + rightsum
        d[i] = score

        if i >= len(nums):
          break

        if nums[i] == 0:
          leftsum += 1
        if nums[i] == 1:
          rightsum -= 1
        
        i += 1
      
      d = list(sorted(d.items(), key= lambda x: -x[1]))
      m = d[0][1]

      res = []

      for k,v in d:
        if v == m:
          res.append(k)
        else:
          break

      return res
        