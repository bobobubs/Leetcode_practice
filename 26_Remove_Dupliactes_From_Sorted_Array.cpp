class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int k = nums.size();
        int i = nums.size() - 1;
        while (i >= 0)
        {
            int j = i - 1; // Start with the final element
            bool foundDuplicate = false;
            while (j >= 0)
            {
                if (nums[i] == nums[j])
                {
                    foundDuplicate = true;
                    break;
                }
                j--;
            }
            if (foundDuplicate)
            {
                nums.erase(nums.begin() + i);
                k--;
            }
            i--;
        }
        return k;
    }
};