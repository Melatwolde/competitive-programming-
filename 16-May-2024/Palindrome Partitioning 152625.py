# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        def partitionHelper(start, s, memo):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [[]]

            result = []
            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if isPalindrome(substring):
                    partitions = partitionHelper(i + 1, s, memo)
                    for partition in partitions:
                        result.append([substring] + partition)

            memo[start] = result
            return result

        memo = {}
        return partitionHelper(0, s, memo)