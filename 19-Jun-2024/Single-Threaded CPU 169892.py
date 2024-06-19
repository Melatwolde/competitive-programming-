# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        tasks = sorted([task + [i] for i, task in enumerate(tasks)], key=lambda x: (x[0], x[1], x[2]))
        
        available = []
        order = []
        time = tasks[0][0]
        i = 0
        
        while len(order) < n:
            while i < n and tasks[i][0] <= time:
                heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if available:
                processing_time, idx = heappop(available)
                time += processing_time
                order.append(idx)
            else:
                time = tasks[i][0]
        
        return order