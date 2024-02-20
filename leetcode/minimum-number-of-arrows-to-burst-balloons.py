class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        count = len(points)
        # for i in points:
        #     while points[i][1] < points[i+1][1] and points[i][0] < points[i+1][1]:
        #         count += 1
        # return count

        y= points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= y:
                y = min(y , points[i][1])
                count -=1
            else:
                y = points[i][1]
        return count