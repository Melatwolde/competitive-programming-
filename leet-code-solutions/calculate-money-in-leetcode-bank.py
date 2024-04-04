class Solution:
    def totalMoney(self, n: int) -> int:
        
        week = n // 7 + (n % 7 != 0)
        answer = 0

        for w in range(week):
            if n < 7:
                for i in range(w + 1, w + 1 + n):
                    answer += i
                n = 0
            
            else:
                for i in range(w + 1, w + 8):
                    answer += i
                
                n -= 7
        return answer
            
