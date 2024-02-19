class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0

        answer = 0
        whites = 0

        for i in range(n - 1, -1, -1):

            if s[i] == "1":
                answer += whites

            else:
                whites += 1

        return answer