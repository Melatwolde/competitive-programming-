class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dp=[[0 for i in range(n)] for j in range(n)]
        degree=[0 for i in range(n)]
        for l in roads:
            degree[l[0]]+=1
            degree[l[1]]+=1
            dp[l[1]][l[0]]=1
            dp[l[0]][l[1]]=1
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                ans=max(ans,degree[i]+degree[j]-dp[i][j])
        return ans
