class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int k = nums.size();
        int i = nums.size() - 2; // start iterating on second to last element
        while (i >= 1)
        { // iterate until the second element
            // if previous, current, and next are all the same
            //  erase current
            if (nums[i] == nums[i - 1] && nums[i] == nums[i + 1])
            {
                nums.erase(nums.begin() + i);
                k--;
            }
            i--;
        }
        return k;
    }
};