class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n

        sorted_intervals = [(interval[0], interval[1], i) for i, interval in enumerate(intervals)]
        sorted_intervals.sort()

        for i in range(n):
            search_end = sorted_intervals[i][1]
            left = i
            right = n - 1
            min_index = -1

            while left <= right:
                mid = (left + right) // 2
                if sorted_intervals[mid][0] >= search_end:
                    min_index = sorted_intervals[mid][2]
                    right = mid - 1
                else:
                    left = mid + 1

            result[sorted_intervals[i][2]] = min_index

        return result