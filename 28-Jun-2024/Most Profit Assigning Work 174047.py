# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        max_= 0
        max_curr= 0
        j = 0

        for i in worker:
            
            while j < len(jobs) and jobs[j][0] <= i:
                max_curr = max(max_curr, jobs[j][1])
                j += 1
            
            max_ += max_curr

        return max_