class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return 0
        if len(nums) <= 3:
            return max(nums)
        rob_last_house = self.rob_helper(nums[1:-2]) + nums[-1]
        not_rob_last_house = self.rob_helper(nums[:-1])
        return max(rob_last_house, not_rob_last_house)

    def rob_helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)        
        past_past, past = nums[0], max(nums[0],nums[1])
        result = 0
        for i in range(2, len(nums)):
            result = max(past, past_past+nums[i])
            past_past, past = past, result
        return result        
