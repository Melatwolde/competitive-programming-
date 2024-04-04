class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def triangle(a,b,c):
            return (a+b >c and a+c > b and b +c > a)
        nums.sort()
        l=len(nums)
        while l>2:
            if triangle(nums[-1],nums[-2],nums[-3]): return sum(nums[i] for i in range(-1,-4,-1))
            nums.pop()
            l-=1
        return 0 