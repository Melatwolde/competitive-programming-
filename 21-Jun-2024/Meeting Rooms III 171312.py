# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used=[0 for _ in range(n)]
        h1=[]
        h2=[]
        meetings.sort()

        for i in range(n):
            heapq.heappush(h1,i)
        
        for i in meetings:
            while len(h2)>0 and h2[0][0]<=i[0]:
                m=heapq.heappop(h2)
                heapq.heappush(h1,m[1])
            if len(h1)>0:
                r=heapq.heappop(h1)
                used[r]+=1
                heapq.heappush(h2,[i[1],r])
            else:
                m=heapq.heappop(h2)
                used[m[1]]+=1
                heapq.heappush(h2,[i[1]+m[0]-i[0],m[1]])
        m=max(used)
        return used.index(m)