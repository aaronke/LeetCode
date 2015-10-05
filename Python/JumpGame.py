class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        max_jump = 0
        for i in range(len(nums)):
            if max_jump < i:
                return False
            if max_jump >= len(nums)-1:
                return True
            max_jump = max(max_jump,i+nums[i])
