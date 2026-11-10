class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        lowpos = 0
        profits = []
        for i, n in enumerate(prices):
            if n < low:
                low = n
                lowpos = i
            profits.append(prices[i] - low)
        print(profits)
        return max(profits)