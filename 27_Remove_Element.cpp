class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = nums.size();
        int i = nums.size() - 1;
        while ( i >= 0) {
            if (nums[i] == val){
                nums.erase(nums.begin() + i);
                k--;
            }
            i--;
        }
        return k;
    }
};