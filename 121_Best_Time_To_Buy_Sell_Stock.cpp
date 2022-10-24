class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int minvalue = INT_MAX;
        for(int i = 0; i<prices.size(); i++){
            //if the current price is lower than current lowest value
            minvalue = min(prices[i],minvalue);
            
            //profit = what was previously calculated or new value if lower
            maxprofit= max(maxprofit,prices[i] - minvalue);
        }
        return maxprofit;
    }
};
