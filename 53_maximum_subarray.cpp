class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int indexMax = nums[0];
        int highestMax = nums[0];
        for (int i = 1; i < nums.size(); i++){
            //see if the contiguous sum of the next number is bigger than next number
            indexMax = max(nums[i], indexMax + nums[i]);
            //see if the current index is bigger than what was highest before.
            highestMax = max(highestMax, indexMax);
        }
        return highestMax;
    }
};