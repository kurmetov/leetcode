class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        current_profit = 0

        for price in prices:
            current_profit = price - min_price
            max_profit = max(current_profit, max_profit)

    
            min_price = min(min_price, price)

        return max_profit


            