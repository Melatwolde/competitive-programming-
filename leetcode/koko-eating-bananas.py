class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(speed):
            hour = 0
            for pile in piles:
                hour +=(pile + speed - 1)//speed
            return hour <= h


        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            
            if checker(mid):
                high = mid 
            else:
                low = mid + 1
        return low