class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger = [0] * 1001

        for trip in trips:
            passenger[trip[1]] += trip[0]
            passenger[trip[2]] -= trip[0]

        cum = 0
        for i in passenger:
            cum += i
            if cum > capacity:
                return False

        return True