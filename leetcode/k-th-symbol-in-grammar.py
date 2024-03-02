class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
 
            if n == 1:
                return 0  
            x_ = self.kthGrammar(n-1, (k+1)//2)
            if x_ == 0:
                return 0 if k %2 == 1 else 1
            else:
                return 1 if k %2  == 1 else 0 
            # nonlocal x_
            # if  n== 1 and k == 1:
            #     return 0
            # mid  = (2**(n-1)) //2
            
            # if k < mid:
            #     x_ = helper(n -1, k)
            # else:
            #     x_ = (helper(n - 1, k - mid))

    
     
            
            