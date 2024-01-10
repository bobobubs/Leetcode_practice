class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for newJump in nums:
            if jump < 0:
                return False
            elif newJump > jump:
                jump = newJump
            jump -=1

        return True