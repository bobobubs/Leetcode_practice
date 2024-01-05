class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i = len(nums) - 2 #starting at the second to last element
        while (i >=  1): #Go to the second element
            #check current, previous, and next
            #if all are the same, remove current.
            if (nums[i] == nums[i - 1] and nums[i] == nums[i + 1]):
                nums.pop(i)
                k -= 1
            i -= 1
        return k