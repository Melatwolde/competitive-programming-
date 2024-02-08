class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pfxsum = [0]*n
        m = len(bookings)
        for start,end,seats in bookings:
            pfxsum[start-1]+=seats
            if end < n : 
                pfxsum[end] -= seats
        for i in range(1,n):
            pfxsum[i] += pfxsum[i-1]
        return pfxsum