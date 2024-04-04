class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(op,cp, curr):
            if op == cp == n:
                res.append("".join(curr))
                return
            if op < n:
                curr.append("(")
                backtrack(op+1, cp, curr)
                curr.pop()
            if cp < op:
                curr.append(")")
                backtrack(op, cp+1, curr)
                curr.pop()
        backtrack (0,0,[])
        return res