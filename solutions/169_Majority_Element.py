class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for i, num in enumerate(nums):
            
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
        return max(elements, key=elements.get)