class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Handle edge cases.
        if k == 0 or len(nums) <= 1:
            return
        else:
            #change large values of k to reasonable values of k
            k = k % len(nums)
            
            #if k is a multiple of len(nums)
            if k == 0:
                return 

            #modify nums.
            front = nums[-k:]
            back = nums[:-k]
            nums[:k] = front
            nums[k:] = back