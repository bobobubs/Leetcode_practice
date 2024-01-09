class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        // handle the edge cases
        int length = prices.size();
        if (length == 2)
        {
            if (prices[1] > prices[0])
            {
                return prices[1] - prices[0];
            }
            else
            {
                return 0;
            }
        }
        if (length == 1)
        {
            return 0;
        }
        int profit = 0;
        for (int i = 0; i < length - 1; ++i)
        {
            if (prices[i] < prices[i + 1])
            {
                profit += prices[i + 1] - prices[i];
            }
        }
        return profit;
    }
};