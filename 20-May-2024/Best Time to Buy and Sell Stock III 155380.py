# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

     
        buy1 = buy2 = float('-inf')
        sell1 , sell2 = 0,0

        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(sell1, buy1 + i)
            buy2 = max(buy2, sell1 - i)
            sell2 = max(sell2, buy2 + i)

        return sell2