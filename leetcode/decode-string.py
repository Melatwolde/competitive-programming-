class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "]":
                stri = ""
                while stack[-1] != "[":
                    stri = stack.pop() + stri
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                Rstri = stri * k
                for j in Rstri:
                    stack.append(j)
            else:
                stack.append(i)
        
        final = "".join(stack)
        return final




        

        
            
        