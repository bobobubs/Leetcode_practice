class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        smallest_value = 100000000 #initialized to a large value to be able to be compared in loop
        for price in prices:
            smallest_value = min(smallest_value, price)
            highest_profit = max(highest_profit, price - smallest_value)
        return highest_profit
