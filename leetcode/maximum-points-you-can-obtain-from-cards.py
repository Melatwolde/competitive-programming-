class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l , r = 0 , len(cardPoints)-k
        totalsum = []
        #sum of the slidig window = n-k
        x = len(cardPoints) -k
        total = sum(cardPoints[x:]) 
        
        res = total
        while r <len(cardPoints):
            total += ( cardPoints[l] - cardPoints[r])
            res = max(res , total)
            l+=1
            r+=1
        return res
        


