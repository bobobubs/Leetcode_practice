class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #handle edge cases
        if(len(prices) == 2):
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        if len(prices) == 1:
            return 0
        
        #now start iterating through the list
        profit = 0
        for i, price in enumerate(prices[:-1]): #disregard the edges
            if prices [i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit