class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_profit = float('inf')
        max_profit = 0

        for price in prices:
            min_profit = min(min_profit, price)
            profit = price - min_profit
            max_profit = max(max_profit, profit)

        return max_profit
        