# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        day = 0
        for i in range(1, len(dp)):
            if i != days[day]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min( dp[max(0, i - 1)] + costs[0],  dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2] )
                day += 1
        return dp[-1]
        # for i,j in zip([1,7,30],costs):
        # for i in range(1, max(days)+1):
        #     if i not in memo:
        #         return memo[i]
        #     memo[i] = min()
