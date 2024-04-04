class Solution:
    def maxIceCream(self, costs, coins):
        max_price = max(costs) 
        count = [0] * (max_price + 1)  

        for price in costs:
            count[price] += 1

        numBars = 0  
        for price in range(len(count)):
            while count[price] > 0 and coins >= price:
                coins -= price
                count[price] -= 1
                numBars += 1

        return numBars