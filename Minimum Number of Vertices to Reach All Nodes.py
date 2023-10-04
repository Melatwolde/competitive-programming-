class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
       classs=[0]*n
       for i in edges:
           classs[i[1]]+= 1
       res=[]
       for j in range(n):
            if classs[j]==0:
                res.append(j)
       return res 
