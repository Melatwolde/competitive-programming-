class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr = [0] + arr + [0]  
        n = len(arr)

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                result += arr[j] * (i - j) * (j - k) 
                result %= MOD
            stack.append(i)

        return result % MOD

                