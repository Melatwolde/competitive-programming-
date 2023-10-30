
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(current, left, right, res):
            if left == 0 and right == 0:
                res.append(current)
                return
            if left > 0:
                generate(current + "(", left - 1, right, res)
            if right > left:
                generate(current + ")", left, right - 1, res)

        res = []
        generate("", n, n, res)
        return res
