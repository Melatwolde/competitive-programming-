# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
            
        engineers = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        maxPerformance = totalSpeed = 0
        minHeap = []

        for s, e in engineers:
            totalSpeed += s
            heapq.heappush(minHeap, s)

            if len(minHeap) > k:
                totalSpeed -= heapq.heappop(minHeap)

            maxPerformance = max(maxPerformance, totalSpeed * e)

        return maxPerformance % (10**9 + 7)