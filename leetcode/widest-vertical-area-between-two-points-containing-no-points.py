class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        m=0
        for x in range(len(points)-1):
            if(points[x+1][0]-points[x][0]>m):
                m=points[x+1][0]-points[x][0]
        return m